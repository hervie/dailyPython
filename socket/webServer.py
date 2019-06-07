import socket

# python 3种字符串：无前缀，u前缀[字符串常量，前缀带不带u，都是一样的], b前缀[必须是十六进制或者ASCII]
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''hello, world! <h1>from hervie's server</h1>'''
response_params = [
    'HTTP/1.1 200 OK',
    'Date: Sun, 27 may 2019 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}.\r\n'.format(len(body.encode())),  # Python encode() 方法以 encoding 指定的编码格式编码字符串。
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen(5)

    print('http://127.0.0.1:8000')

    try:
        while True:
            conn, addr = server.accept()
            handle_connection(conn, addr)
    finally:
        server.close()


if __name__ == '__main__':
    main()
