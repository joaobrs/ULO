from setuptools import setup, Extension
import numpy

core = Extension('ulo.core',
                 ['./ulo/core.c'],
                 extra_compile_args=["-Ofast", "-march=native"],
                 include_dirs=[numpy.get_include()])

setup(
    name="ulo",
    version="0.1.1",
    packages=["ulo"],
    test_suite="tests",
    author="Pete Shadbolt",
    author_email="hello@peteshadbolt.co.uk",
    url="https://github.com/peteshadbolt/ulo",
    description="Linear optics simulator",
    keywords="quantum",
    scripts=[],
    package_data={},
    ext_modules=[core],
    include_package_data=False
)
