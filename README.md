<p align="center">
    <img src="./readme_header.png" width="450" alt="Link 4 Online">
</p>

# Link 4 Online
『Connect 4』が遊べるオンラインゲームです。
WebSocket と Vue.js の学習で作りました。

[ English README is here ](./README_en.md)
## 技術スタック
### フロントエンド
- TypeScript
- pnpm
- Vite
- Vue.js
- VueRouter
### バックエンド
- Python
- FastAPI
- Pydantic
- uvicorn
- websockets

## 実行方法 (Docker)
### Dev
`compose.yml` を使って開発コンテナを起動する
```bash
docker compose up
```
### Build
`package.json`の`production`スクリプト を使ってビルドしたコンテナを起動する
```bash
pnpm production
```

## License
Private / Personal project
