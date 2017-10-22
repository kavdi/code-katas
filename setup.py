from setuptools import setup



setup(
    name='code-katas',
    description='A package for building and running the katas functions',
    package_dir={'':'katas'},
    author='Kavdi',
    author_email='kavdyjh@gmail.com',
    py_modules=['katas'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython', 'faker']
    },
    
)