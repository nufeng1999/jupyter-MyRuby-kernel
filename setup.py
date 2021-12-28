from setuptools import setup

setup(name='jupyter_MyRuby_kernel',
      verbion='0.0.1',
      description='Minimalistic Ruby kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifierb=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyRuby-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyRuby-kernel/tarball/0.0.1',
      packages=['jupyter_MyRuby_kernel'],
      scripts=['jupyter_MyRuby_kernel/install_MyRuby_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'ruby','rb'],
      include_package_data=True
      )
