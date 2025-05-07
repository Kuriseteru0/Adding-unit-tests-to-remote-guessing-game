from game_logic import evaluate_guess


def start_server(number_to_guess=None):
    import socket
    import random

    host = '127.0.0.1'
    port = 65432
    number_to_guess = number_to_guess or random.randint(1, 100)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server started. Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                guess = int(data)
                response = evaluate_guess(guess, number_to_guess)
                conn.sendall(response.encode())
