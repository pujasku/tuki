from setuptools import setup, find_packages

setup(
    name='tuki',
    version='0.1',
    description='a simple static website generator',
    author='pujasku',
    author_email='pujasku@gmail.com',
    packages=find_packages(),
    install_requires=[
        "markdown"
    ],
    entry_points={
        'console_scripts': [
            'tuki = tuki.main:main'
        ]
    },
    include_package_data=True,
)

