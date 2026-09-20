from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketException,
    WebSocketDisconnect,
    status,
)
from room_manager import RoomManager
from room import Room
from session_manager import SessionManager
from session import Session
from schemas.network import UserMessage
from pydantic import TypeAdapter, ValidationError

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

router = APIRouter(prefix="", tags=["websocket"])


@router.websocket("/room/{room_id:path}")
async def _(room_id: str, ws: WebSocket):
    origin = ws.headers.get("origin")
    if origin not in ALLOWED_ORIGINS:
        print(f"{origin} is not in ALLOWED_ORIGINS")
        await ws.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    await ws.accept()
    if not room_id.isdigit():
        print("room_id is not number")
        raise WebSocketException(code=1008, reason="room_id is not number")
    if not isinstance(RoomManager.search_room_by_id(int(room_id)), Room):
        print("undefined room")
        raise WebSocketException(code=1008, reason="undefined room")
    if not RoomManager.can_join_room(int(room_id)):
        print("can not join room")
        raise WebSocketException(code=1008, reason="can not join room")
    print("ws.accept")

    print("room_id is number", room_id)
    session = SessionManager.create_session(ws, int(room_id))
    if not isinstance(session, Session):
        print("did not create Session")
        return await ws.close(code=1008, reason="did not create Session")
    try:
        while True:
            message = await session.ws.receive_json()
            # print("message:",message)
            try:
                if TypeAdapter(UserMessage).validate_python(message):
                    await session.handlle_message(UserMessage(message))
            except ValidationError as e:
                print("EXception:", e)
                print("message:", message)
    except WebSocketDisconnect:
        await session.exit_room()
    except RuntimeError as error:
        if not SessionManager.search_session_by_id(session.id):
            return print("session was closed")
        print("catch runtime error:", error)
        print(error.__class__.__name__)
    except Exception as e:
        print("server session error:", e)
