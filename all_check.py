#!/usr/bin/env python3
import os
import sys

def check_reboot():
  """Rerturns T if the computer has a pending reboot!"""
  return os.path.exists('*/run/reboot-required')

def main():
  if check_reboot():
<<<<<<< HEAD
    print("this is just a test code!")
=======
    print("this is just a test code!!")
>>>>>>> c8bffb12a39ebd9844ad6c8bb988a96cd770ff90
    print("Reboot is pending")
    print("All ok")
    print("Author: Dilip singh Kushwah")
    sys.exit(1)

main()
