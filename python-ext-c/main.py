from ctypes import cdll

lib = cdll.LoadLibrary('./adder.so')

print(lib.add(3,'a'))
