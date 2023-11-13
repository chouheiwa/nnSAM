import socket
from visualdl.server import app

from nnunetv2.paths import nnUNet_logs, nnUNet_visual_port


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def start_server(port=nnUNet_visual_port):
    if port is None:
        port = find_free_port()
    app.run(
        nnUNet_logs,
        host='0.0.0.0',
        port=port,
    )


if __name__ == '__main__':
    start_server()
