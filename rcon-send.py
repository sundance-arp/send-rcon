#!/usr/bin/python3
import socket
import getpass


def construct_auth(password):
    payload = encode_payload(0, 3, password)
    return payload


def construct_execcommand(command):
    payload = encode_payload(0, 2, command)
    return payload


def encode_payload(data_id, data_type, data_body):
    data = b''
    data += data_id.to_bytes(4, 'little')
    data += data_type.to_bytes(4, 'little')
    data += data_body.encode('ascii') + b'\x00'

    payload = len(data).to_bytes(4, 'little') + data

    return payload


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        password = getpass.getpass()
        sock.connect(('127.0.0.1', 25575))

        sock.sendall(construct_auth(password))
        data = sock.recv(1024)
        print('---auth response---')
        print(data)

        sock.sendall(construct_execcommand('gamemode survival Bushisaki'))
        data = sock.recv(10000)
        print('---execcommand response---')
        print(data)

        sock.sendall(construct_execcommand('gamemode creative Bushisaki'))
        data = sock.recv(10000)
        print('---execcommand response---')
        print(data)

        sock.sendall(construct_execcommand('gamemode survival Bushisaki'))
        data = sock.recv(10000)
        print('---execcommand response---')
        print(data)

        sock.sendall(construct_execcommand('gamemode creative Bushisaki'))
        data = sock.recv(10000)
        print('---execcommand response---')
        print(data)

        sock.sendall(construct_execcommand('say KUMA'))
        data = sock.recv(10000)
        print('---execcommand response---')
        print(data)


if __name__ == '__main__':
    main()
