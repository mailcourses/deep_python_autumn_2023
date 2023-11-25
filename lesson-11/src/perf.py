#! /usr/bin/env python3

import time
import ctypes

import cffi
import cutils
import cyutils

N = 36

def fibonacci(n: int):
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def native_python():
    start_ts = time.time()
    res = fibonacci(N)
    end_ts = time.time()
    print(f"[python] Time of execution is {end_ts - start_ts} seconds")
    return res

def ctypes_fibonacci():
    utils_lib = ctypes.cdll.LoadLibrary('./ctypes_lib/libutils.so')
    utils_lib.fibonacci.restype = ctypes.c_int
    utils_lib.fibonacci.argstype = [ctypes.c_int]
    start_ts = time.time()
    res = utils_lib.fibonacci(N)
    end_ts = time.time()
    print(f"[ctypes] Time of execution is {end_ts - start_ts} seconds")
    return res

def cffi_fibonacci():
    ffi = cffi.FFI()
    lib = ffi.dlopen('./ctypes_lib/libutils.so')
    ffi.cdef('''
    int fibonacci(int n);
    ''')

    start_ts = time.time()
    res = lib.fibonacci(N)
    end_ts = time.time()
    print(f"[cffi] Time of execution is {end_ts - start_ts} seconds")
    return res

def capi_fibonacci():
    start_ts = time.time()
    res = cutils.fibonacci(N)
    end_ts = time.time()
    print(f"[capi] Time of execution is {end_ts - start_ts} seconds")
    return res

def cython_fibonacci():
    start_ts = time.time()
    res = cyutils.fibonacci(N)
    end_ts = time.time()
    print(f"[cython] Time of execution is {end_ts - start_ts} seconds")
    return res

def main():
    py_res = native_python()
    ctypes_res = ctypes_fibonacci()
    cffi_res = cffi_fibonacci()
    capi_res = capi_fibonacci()
    cython_res = cython_fibonacci()
    print(f"Res is {py_res}")
    assert(py_res == ctypes_res == cffi_res == capi_res == cython_res)

if __name__ == "__main__":
    main()
