<p align="center">
    <img src="./public/readme_header.png" width="450" alt="Link 4 Online">
</p>

# Link 4 Online
This is an online game where you can play Connect 4.
I created this repository to learn WebSocket and Vue.js.

[ 日本語のREADMEはこちら ](./README.md)
## Tech stack
### Frontend
- language: TypeScript
- package manager: pnpm
- Vite
- Vue
- VueRouter
### Backend
- language: Python
- FastAPI
- Pydantic
- uvicorn
- websockets

## Setup
1. Install frontend dependencies
    ```bash
    pnpm i # or pnpm install
    ```
2. Install backend dependencies

    If you use venv, make sure to activate it before running the command.
    ```bash
    pip install -r requirements.txt
    ```
## How to run
### Dev
1. Run the Python server

    If you use venv, make sure to activate it before running the command.
    ```bash
    pnpm backend
    ```
2. Open a new terminal tab and run the Vite dev server
    ```bash
    pnpm dev
    ```

    You can access the site at `http://localhost:5173`.
### Build
1. Build the frontend
    ```bash
    pnpm build
    ```
2. Run the Python server

    If you use venv, make sure to activate it before running the command.
    ```bash
    pnpm backend
    ```
    You can access the built site at `http://localhost:8000`.
## License
Private / Personal project
