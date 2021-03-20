#!/usr/bin/env python3
import os
import sys

def check_reboot():
  """Rerturns T if the computer has a pending reboot!"""
  return os.path.exists('*/run/reboot-required')

def main():
  if check_reboot():
    print("this is just a test code!!")
    print("Reboot is pending")
    print("All ok")
    print("Author: Dilip singh Kushwah")
    sys.exit(1)

main()
