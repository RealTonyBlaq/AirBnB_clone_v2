#!/usr/bin/python3

num = "10000"
flo = "10.22"
string = "okay"

a_list = [num, flo, string]

for value in a_list:
    if value.isdigit():
        value = int(value)
        print(type(value))
    else:
        try:
            value = float(value)
            print(value, type(value))
        except ValueError:
            print(value)
