from setuptools import setup

setup(name='scanningegs',
      version='0.0.4',
      description='Generate EGSnrc files for a scanning target',
      url='http://github.com/henrybaxter/scanningegs',
      author='Henry Baxter',
      author_email='henry.baxter@gmail.com',
      license='MIT',
      packages=['scanningegs'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['scanningegs=scanningegs.scanningegs:main']
      },
      install_requires=['toml'])
