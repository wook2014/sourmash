import os

from setuptools import setup
from setuptools_rust import RustExtension, Binding


# "None" will use setuptools_rust autodetection
# (debug for develop, release for install)
DEBUG_BUILD = True if os.environ.get("SOURMASH_DEBUG") == "1" else None


setup(
  package_dir={"": "src"},
  entry_points={
    'console_scripts': [
      'sourmash = sourmash.__main__:main'
    ],
    'distutils.setup_keywords': [
      'universal_wheel = sourmash.dist:universal_wheel',
    ],
  },
  rust_extensions=[
    RustExtension("sourmash._lowlevel__lib",
                  py_limited_api="auto",
                  path="src/core/Cargo.toml",
                  binding=Binding.NoBinding,
                  debug=DEBUG_BUILD,
                  ),
  ],
  cffi_modules=["src/sourmash/ffi_build.py:ffibuilder"],
  universal_wheel=True
)
