#!/usr/bin/env python

from os import environ
from distutils.core import setup
from setuptools import setup
from setuptools import find_packages
# from torch.utils.cpp_extension import BuildExtension, CUDAExtension


environ['TORCH_CUDA_ARCH_LIST']="7.0+PTX"
setup(name='TRAK',
    version='0.1.0',
    description="TRAK: Understanding Model Predictions at Scale",
    author='MadryLab',
    author_email='krisgrg@mit.edu',
    license_files=('LICENSE.txt', ),
    packages=['traker'],
    install_requires=
        ['torch',
        'numpy',
        'tqdm'
        ],
    extras_require = {
        'tests':
        ["assertpy",
         "torchvision",
         "open_clip_torch",
        ]}
    # ext_modules=[
        # CUDAExtension('fast_jl', [
            # 'fast_jl/fast_jl.cpp',
            # 'fast_jl/fast_jl_kernel.cu',
        # ]),
    # ],
    # cmdclass={
       # 'build_ext': BuildExtension
    # }
    )
