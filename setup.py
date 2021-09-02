from setuptools import setup, find_packages

setup(
    name='f21-se-hw2b',
    version='0.1',
    description='Enjoy some Chuck Norris jokes',
    author='Sharath Kumar',
    author_email='svkumar2@ncsu.edu',
    packages=find_packages(where='code'),
    package_dir={"":"code"},
    extras_require=dict(request='requests')
)
