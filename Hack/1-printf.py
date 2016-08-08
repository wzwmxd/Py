from ctypes import *


class struct_a(Structure):
    _fields_ = [
        ('a', c_int),
        ('b', c_int),
    ]


a = struct_a(1, 2)
msvcrt = cdll.msvcrt
message_string = 'Hello world!\n'
msvcrt.printf("Testing: %s a.a=%d,a.b=%d", message_string, a.a, a.b)
