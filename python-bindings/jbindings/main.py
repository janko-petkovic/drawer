import ctypes
import example_jmath

if __name__ == '__main__':
    lib = example_jmath.lib
    # lib.add.restype = ctypes.c_float
    # lib.subtract.restype = ctypes.c_float
    # lib.multiply.restype = ctypes.c_float
    # lib.divide.restype = ctypes.c_float
    lib.add(8,4)
    lib.subtract(8,4)
    lib.multiply(8,4)
    lib.divide(8,4)
