from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='nCoV',
      version='0.1.7',
      author='Yifan Yang',
      author_email='yangyifan529@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      description='Get instant information about 2019-nCoV',
      url="https://github.com/EthanGeekFan/nCoV",
      packages=find_packages(),
      install_requires=['click', 'beautifulsoup4', 'prettytable'],
      entry_points={
          'console_scripts': [
              'nCoV=Report.__main__:main'
          ],
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable"
      ],
      )
