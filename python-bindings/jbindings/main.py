import ctypes

if __name__ == '__main__':
    lib = ctypes.CDLL('./libjmath.so')
    lib.add.restype = ctypes.c_float
    lib.subtract.restype = ctypes.c_float
    lib.multiply.restype = ctypes.c_float
    lib.divide.restype = ctypes.c_float
    lib.add(ctypes.c_float(8),ctypes.c_float(4))
    lib.subtract(ctypes.c_float(8),ctypes.c_float(4))
    lib.multiply(ctypes.c_float(8),ctypes.c_float(4))
    lib.divide(ctypes.c_float(8),ctypes.c_float(4))
