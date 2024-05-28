#!/usr/bin/env python3
import os
import sys

# LBYL - Lookk Before you leap

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] file names.txt not found")
    sys.exit()


# LBYL - Lookk Before you leap

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit()
