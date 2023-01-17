# Connect to this server using echo "foobar" | nc localhost 8080 -q 1

import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
  with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(BYTES_TO_READ)
        if not data:
          break
        print(data)
        conn.sendall(data)
  return

def start_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows socket to reuse a connection
    s.listen()

    conn, addr = s.accept()
    handle_connection(conn, addr)

  return

def start_threaded_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows socket to reuse a connection
    s.listen(2)
    while True:
      conn, addr = s.accept()
      thread = Thread(target=handle_connection, args=(conn, addr))
      thread.run()

# start_server()
start_threaded_server()