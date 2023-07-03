# main.py
import uvicorn


async def app(scope, receive, send):
    return

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
