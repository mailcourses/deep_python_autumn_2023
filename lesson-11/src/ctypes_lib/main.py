import ctypes

def main():
    utils_lib = ctypes.cdll.LoadLibrary('./libutils.so')
    utils_lib.sum.restype = ctypes.c_int
    utils_lib.sum.argstype = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

    lst = list(range(0, 5))
    len_lst = len(lst)
    arr_int_type = ctypes.c_int * len_lst
    res = utils_lib.sum(arr_int_type(*lst), len_lst)
    print(f"Result of ctypes lib is {res}")

    utils_lib.fibonacci.restype = ctypes.c_int
    utils_lib.fibonacci.argstype = [ctypes.c_int]

    res = utils_lib.fibonacci(10)
    print(f"Res of fibonacci is {res}")


if __name__ == "__main__":
    main()
