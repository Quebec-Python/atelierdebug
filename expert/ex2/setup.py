from distutils.core import setup, Extension

# define the extension module
cos_module = Extension('ex2', sources=['ex2.c'],
                       extra_compile_args=["-O2", "-Wall", "-Werror", "-pedantic", "-march=native", "-fpic", "-std=c11", "-shared", "-g"])

# run the setup
setup(ext_modules=[cos_module])
