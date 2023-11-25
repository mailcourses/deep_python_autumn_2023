from setuptools import setup, Extension
from Cython.Build import cythonize

def main():
    setup(
        ext_modules=cythonize(['cyutils.pyx'])
    )

if __name__ == "__main__":
    main()
