import setuptools


setuptools.setup(
    name='flake8-asserts',
    license='MIT',
    version='0.1.0',
    author='Jon Dufresne',
    author_email='jon.dufresne@gmail.com',
    py_modules=['flake8_asserts'],
    install_requires=[
        'flake8 > 3.0.0',
    ],
    entry_points={
        'flake8.extension': [
            'A = flake8_asserts:Flake8AssertsPlugin',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
