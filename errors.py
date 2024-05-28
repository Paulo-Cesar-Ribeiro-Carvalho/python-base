#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASK Forgiveness than permission


try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit()
    # TODO: Usar retray
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit()
