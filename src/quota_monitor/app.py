import threading
import webbrowser

from .server import create_server


def main():
    server = create_server()
    port = server.server_address[1]
    url = f"http://127.0.0.1:{port}"
    print(f"OpenAI Free Credit Tracker: {url}")
    print("Close this window to stop the local server.")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
