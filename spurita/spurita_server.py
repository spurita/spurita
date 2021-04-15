import os

from spurita.api.spurita_api_server import create_api_server

spurita_api_server, spurita_socketio = create_api_server()

if __name__ == "__main__":
    spurita_socketio.run(spurita_api_server, port=os.getenv("PORT", 5000))
