from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0',
    description='A simple dice game simulator',
    author='Thomas Flynn',
    author_email='tflynn@virginia.edu',
    url='https://github.com/your-username/dice-game',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.2.0',
        'numpy>=1.20.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
