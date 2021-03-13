#!/usr/bin/env python3
import os
import sys

def check_reboot():
  """Rerturns T if the computer has a pending reboot!"""
  return os.path.exists('*/run/reboot-required')

def main():
  if check_reboot():
    print("Reboot is pending")
    sys.exit(1)

main()
