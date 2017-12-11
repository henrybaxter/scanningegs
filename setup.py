from setuptools import setup

setup(name='scanningegsinp',
      version='0.2.4',
      description='Generate EGSINP files for a scanning target',
      url='http://github.com/henrybaxter/scanningegsinp',
      author='Henry Baxter',
      author_email='henry.baxter@gmail.com',
      license='MIT',
      packages=['scanningegsinp'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['scanningegsinp=scanningegsinp.scanningegsinp:main']
      },
      install_requires=['toml'])
