from ipykernel.kernelapp import IPKernelApp
from .kernel import RubyKernel
IPKernelApp.launch_instance(kernel_class=RubyKernel)
