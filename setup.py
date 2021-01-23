from setuptools import setup,find_packages

with open("README.md", 'r') as f:
    README = f.read()

setup(
   name='oitool',
   version='0.1.0',
   description='Utilities for the analysis of Option data',
   license="MIT",
   long_description=README,
   long_description_content_type='text/markdown',
   author='Chiranjeev',
   author_email='stockalgos@gmail.com',
   project_urls={
          "Organization":"http://www.bandl.io",
          "Source":"https://github.com/stockalgo/OItool",
          "Tracker":"https://github.com/stockalgo/OItool/issues"
          },
   packages=find_packages('lib'),
   package_dir = {'':'lib'},
   include_package_data=True,
   install_requires=[
            'bandl',
            'influxdb'],
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
        ],
    download_url = "",
    keywords = ["python","option","nse","open-interest","open-interest-charts"]
)