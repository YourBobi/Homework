from setuptools import setup, find_packages
import RR

with open("./README.md") as readmeFile:
    readme = readmeFile.read()

setup(
    name='RR',
    author='Selivonchyk Kolya',
    author_email=['still_student@mail.ru'],
    version=RR.__version__,
    description="Parsing https://vse.sale/news/rss",
    long_description=readme,

    packages=["RR", "tests"],
    test_suite="tests.run",
    scripts=["RR/rss_reader.py"],
    entry_points={
        'console_scripts':
            ['RR = RR:main',
             'pytest-runner = tests:run']
    },
    install_requires=[
        'pytest>=6.2.5',
        'bs4>=0.0.1',
        'dominate>=2.6.0',
        'FB2>=0.1.7',
        'urllib3>=1.26.7',
        'lxml>=4.6.3'
    ],
    python_requires='>=3.9'
)
