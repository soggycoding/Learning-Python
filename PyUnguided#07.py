#New project, I will try to make a lyrics typing output where I will understand the time module and delays
import sys
import time

with open('Documents/wiwiws.txt', mode='r', encoding="utf-8") as file:
    for line in file:
        line.strip()
        for char in line:
            sys.stdout.flush()
            print(char, end="")
            time.sleep(0.08)