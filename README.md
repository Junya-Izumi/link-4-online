<p align="center">
    <img src="./public/readme_header.png" width="450" alt="Link 4 Onilne">
</p>

# Link 4 Online
『Connect 4』が遊べるオンラインゲームです。
WebSocket と Vue.js の学習で作りました。
## 技術スタック
### フロントエンド
- 言語: TypeScript
- パッケージマネージャ: pnpm
- Vite
- Vue
- VueRouter
### バックエンド
- 言語: Python
- FastAPI
- Pydantic
- uvicorn
- websockets

## セットアップ
1. pnpm の依存パッケージをインストールします
    ```bash
    pnpm i # or pnpm install
    ```
2. python の依存パッケージをインストールします

    venvを利用する場合はインストールする前にvenvをアクティベートしてください
    ```bash
    pip install -r requirements.txt
    ```
## 実行方法
### dev
1. python サーバーを起動する

    venvを利用する場合は実行する前にvenvをアクティベートしてください
    ```bash
    pnpm backend
    ```
2. 新しいタブをでViteの開発サーバーを起動する
    ```bash
    pnpm dev
    ```

`http://localhost:5173`でサイトにアクセスすることができます
### build
1. フロントエンドのファイルをビルドします
    ```bash
    pnpm build
    ```
2. python サーバーを起動する
    
    venvを利用する場合は実行する前にvenvをアクティベートしてください
    ```bash
    pnpm backend
    ```
`http://localhost:8000`でビルドしたサイトにアクセスできます

## License
Private / Personal project