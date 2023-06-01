#!/usr/bin/python3
for i in range(0, 99):
    print(f"0{i}, ", end="") if i < 10 else print(f"{i}, ", end="")
print("99")
