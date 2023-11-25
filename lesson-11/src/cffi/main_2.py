#! /usr/bin/env python3

import cffi

def main():
    ffibuilder = cffi.FFI()
    ffibuilder.cdef('''
    int mult(int* arr, int len);
    ''')

    ffibuilder.set_source('tmp_utils',
    '''
    int mult(int* arr, int len)
    {
        int res = 1;
        for (int i = 0; i < len; ++i)
        {
            res *= arr[i];
        }
        return res;
    }
    ''')
    ffibuilder.compile()

if __name__ == "__main__":
    main()
