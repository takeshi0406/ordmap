from setuptools import setup, find_packages

setup(
    name='ordmap',
    description="Visualise your task Loasmap as Hasse Diagram.,
    version='0.0.1',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ordmap = ordmap.cli:main'
        ]
    ],
    author='takeshi0406',
    author_email='sci.and.eng@gmail.com',
    url='https://github.com/takeshi0406/ordmap',
    install_requires=['networkx', 'matplotlib', 'pyyaml'],
    test_suite='tests',
)
