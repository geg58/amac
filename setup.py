from setuptools import setup, find_packages

tests_require = [
    'flake8',
    'nose',
    'mock',
    'nose-timer'
]

setup(
    name='amac-ca',
    version='0.0.1',
    description="Open-source self-driving car",
    author=(
         "Travis Brashears, "
         "Bradley Qu, "
         "Daniel Shen"),
    author_email=(
         "trbrashears@berkeley.edu, "
         "qu.bradley@berkeley.edu, "
         "daniel.shen@berkeley.edu"),
    packages=find_packages(),
    install_requires=[
        'pyserial'],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={
            },
    )
