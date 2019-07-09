#!/usr/bin/env python3
import socket
import getpass
import random
import argparse
import sys

import send_rcon


def init_args():
    parser = argparse.ArgumentParser(description='do not pop monster')
    parser.add_argument('address')
    parser.add_argument('port')
    parser.add_argument('user')
    args = parser.parse_args()
    return args


def execute_command(commad, sock, data_id):
    payload = send_rcon.construct_execcommand(data_id, command)
    data = send_rcon.send_rcon(sock, payload)
    return data


args = init_args()
password = getpass.getpass()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((args.address, int(args.port)))
    data_id = random.randint(0x00000000, 0xFFFFFFFE)
    data = None

    payload = send_rcon.construct_auth(data_id, password)
    data = send_rcon.send_rcon(sock, payload)
    if not send_rcon.is_authentication_success(data_id, data):
        print("Authentication failed.")
        exit(1)
    print("Authentication succeeded.")

    print('')

    execute_range = 100
    execute_height = 30

    for x in range(-execute_range, execute_range + 1):
        for z in range(-execute_range, execute_range + 1):
            if (x % 6 == 0) and (z % 6 == 0):
                for y in range(-execute_height, execute_height + 1):
                    command = "execute at %s if block ~%d ~%d ~%d minecraft:cave_air run setblock ~%d ~%d ~%d minecraft:torch" % (args.user, x, y, z, x, y, z)
                    data = execute_command(command, sock, data_id)
                    if 'Changed the block' in data[8:].decode():
                        print(data[8:].decode())
                        break
                    command = "execute at %s if block ~%d ~%d ~%d minecraft:air run setblock ~%d ~%d ~%d minecraft:torch" % (args.user, x, y, z, x, y, z)
                    data = execute_command(command, sock, data_id)
                    if 'Changed the block' in data[8:].decode():
                        print(data[8:].decode())
                        break
                    command = "execute at %s if block ~%d ~%d ~%d minecraft:grass run setblock ~%d ~%d ~%d minecraft:torch" % (args.user, x, y, z, x, y, z)
                    data = execute_command(command, sock, data_id)
                    if 'Changed the block' in data[8:].decode():
                        print(data[8:].decode())
                        break
                    command = "execute at %s if block ~%d ~%d ~%d minecraft:tallgrass run setblock ~%d ~%d ~%d minecraft:torch" % (args.user, x, y, z, x, y, z)
                    data = execute_command(command, sock, data_id)
                    if 'Changed the block' in data[8:].decode():
                        print(data[8:].decode())
                        break
