import cffi
import glob
import invoke
import os
import pathlib
import re


@invoke.task # type: ignore
def clean(c, path=None):
    print('==> Cleaning up.')
    for file_pattern in (
        "*.o",
        "*.so",
        "example_*",
    ):
        print(f'  -> removing files: {file_pattern}')
        for file in glob.glob(file_pattern):
            os.remove(file)


@invoke.task # type: ignore
def build_jmath(c, path=None):
    print('==> Building C library: libjmath.so')
    # I don't know while we do two step compilation
    invoke.run("gcc -O3 -c -Wall -Werror -fPIC jmath.c")
    invoke.run("gcc -shared jmath.o -o libjmath.so")


@invoke.task(build_jmath) # type: ignore
def build_jmath_cffi(c, path=None):
    print('==> Building Python module: jmath')

    this_folder = pathlib.Path().resolve()
    hpp_file_name = this_folder / 'jmath.h'
    ffi = cffi.FFI()

    with open(hpp_file_name) as hpp_file:
        lns = hpp_file.read().splitlines()

        flt = filter(
            lambda ln: not re.match(r" *#", ln),
            lns,
        )

        ffi.cdef(str("\n").join(flt))

    ffi.set_source(
        'example_jmath',
        '#include "jmath.h"',
        libraries=['jmath'],
        library_dirs=['.'],
        extra_link_args=['-Wl,-rpath,.']
    )

    ffi.compile()
