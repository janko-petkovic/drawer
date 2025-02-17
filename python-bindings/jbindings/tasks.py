import invoke
import cffi

def print_banner(msg):
    print("="*40)
    print(f"= {msg}")

@invoke.task
def build_jmath(c, path=None):
    print_banner('Building C++ library: jmath')
    # I don't know while we do two step compilation
    invoke.run("g++ -c -Wall -Werror -fPIC jmath.cpp")
    invoke.run("g++ -shared jmath.o -o libjmath.so")
    invoke.run("rm jmath.o")
    print("* Complete")

@invoke.task
def build_jmath_cffi(c, path=None):
    print_banner('Building Python module: jmath')

    ffi = cffi.FFI()

    with open('./jmath.hpp') as hppfile:
        ffi.cdef(hppfile.read())

    ffi.set_source(
        'jmath',
        '#include "jmath.hpp"',
        libraries=['jmath'],
        library_dirs=['.'],
        extra_link_args=['-Wl, -rpath, .']
    )

    ffi.compile()
    print("* Complete")
