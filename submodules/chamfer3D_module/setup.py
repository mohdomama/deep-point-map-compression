from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


setup(
    name='chamfer_3D',
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('chamfer_3D', [
            "/".join(__file__.split('/')[:-1] + ['chamfer3D/chamfer_cuda.cpp']),
            "/".join(__file__.split('/')[:-1] + ['chamfer3D/chamfer3D.cu']),
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
    )
