#!/usr/bin/env python3
import os
import sys
import shutil

def memory_info():
    total, used, free = shutil.disk_usage("/mnt/c")
    print("Total: %d Gib" % (total // (2**30)))
    print("Used: %d Gib" % (used // (2**30)))
    print("Free: %d Gib" % (free // (2**30)))

def main():
    memory_info()

main()
