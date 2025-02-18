# Notes on python bindings

## General considerations

There's a number of ways to do bindings, some are quicker, some are more flexible.

Three good reasons to bind C++ code to python:

1. you already have a ton of C++ code

2. you want to speed up python

3. you want to use python testing

**Marshalling:** the process of transforming the memory representation of an object to a data format suitable for storage or transmission.

Clearly, when we move data from C to Python and vice versa we need to move it using suitable memory representations.

Some caveats:

- **integers:** Python stores with arbitrary precision, while C specifies the int size. Careful not to overflow when moving from Python to C

- **Floating-point numbers**: again, pay attention to overflowing when going from Python to C

- **Complex numbers**: C++ has no native complex data type, you'll need to create a class

- **Strings:** good luck, you have to find ad-hoc solutions case by case - also notice that C and C++ behave differently in regard to strings

- **Boolean:** no caveats here

**Mutable vs immutable values:** Something I didn't know, is that C does not have the pass-by-reference semantics - instead, you have to explicitly pass the pointer. 

All in all, C will only take immutable objects, also from Python. Forget passing a poiinter since pointers in Python are quite non portable to get.

**Memory management:** Python is garbage collected while in C you need to remember to do it manually.



## Let's write some code

`invoke` super cool tool that should have a similar purpose to `make` (with its `cmake`).

You can install it via `pip` as usual.

It relies on a file called `tasks.py` describing all the routines that can be executed via the call `invoke <task-name>`. To see the possible routines, run `invoke --list`. 

Before all of this, let's first see a more down to earth approach.

### `ctypes` module

You write your library in C or C++ , compile it _as a dynamically linked library_ (`.dll` on windows, `.so` on linux) and then import it in the python script. Here's an example:

1. header. Notice the `__cplusplus` and `extern "C"` semantics - if you skip it, you will not be able to call the function in the python code ([more info here](https://stackoverflow.com/questions/10422034/when-to-use-extern-in-c)).

```cpp
// mafs.hpp

#ifdef __cplusplus
extern "C" {
#endif

float adder(float a, float b);

#ifdef __cplusplus
}
#endif
```

2. implementation `adder.cpp`

```cpp
// mafs.cpp

#include <iostream>
#include "adder.hpp"


float adder(float a, float b) {
    float result = a + b;
    std::cout << a << " + " << b << " = " << result << std::endl;
    return result;
}
```

3. compile to shared library: `g++ -fPIC -shared mafs.cpp -o libmafs.so`

4. Include in the python script via the `ctypes` module

```python
# main.py

import ctypes

if __name__ == '__main__':
    lib = ctypes.CDLL('./libmafs.so')
    lib.adder.restype = ctypes.c_float # marshalling output
    lib.adder(ctypes.c_float(3),ctypes.c_float(4)) # marshalling input
```

A very cute addition regards the compilation step. Instead of writing it with our own fingers each and every time, we can start using `invoke`

```python
# tasks.py

@invoke.task
def build_mafs(c, path=None):

    print('Building C++ library: mafs')

    # I don't know while we do two step compilation
    invoke.run("g++ -c -Wall -Werror -fPIC mafs.cpp")
    invoke.run("g++ -shared mafs.o -o libjmafs.so")

    # optionally remove the objects
    invoke.run("rm jmath.o") 

    print("* Complete")
```

After saving, we can now run `invoke build-adder` (you can also find it in the `invoke --list` command list) and build everything. Not super useful for now but it will get better. Also, for now I have no idea about the signature of the library builders, I'm just copypasting.

So, `ctypes` is nice for small things, and it's also handy because it's already present in the python standard library. Let's now find a way to manage bigger things.

### `CFFI` module (C Forein Function Interface)

Important: this is only for C! I have not managed to run it with C++ due to the fact that C++ needs the `extern "C" {...}`. This cannot be handled by `CFFI`.

There are multiple ways to use this interface:

- API vs ABI (the first recompiles the C code, the second just loads the shared libraries). Everyone recommends using API

- in-line (compiles the bindings every time the python script runs) vs out-of-line mode (explicitly manage binding generation once. The generated code then just gets called in the python script)

We will use **API out-of-line mode** - which is generally the recommended way to go.

`CFFI` is different from `ctypes` as it creates a full Python module, instead of just loading some executables in a wrapper (I think).

As far as I understand, the main work happens in the `tasks.py` file, with the source files being left as they are.

```python
# tasks.py

import cffi

@invoke.task(build_mafs) # notice how we first compile the .so from C
def build_mafs_cffi(c, path=None):

    print('Building Python module: mafs')
    ffi = cffi.FFI()

    # (1)
    with open('./mafs.h') as hfile:
        ffi.cdef(hppfile)

    # (2)
    ffi.set_source(
        'mafs_module', # name of the python module
        '#include "mafs.h"', # for now we need this, can be customized
        libraries=['mafs'], # name of the C shared lib (build_mafs!)
        library_dirs=['.'], # folders with libraries
        extra_link_args=['-Wl,-rpath,.'], # look here for additional libs you need to load
    )

    # (3)
    ffi.compile()
```

1. CFFI provides an automated routine for **parsing the headers** and **understanding automatically the datatypes** that well need to be marshalled (automatically creates marshalling wrappers)
