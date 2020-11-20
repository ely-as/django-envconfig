from setuptools import find_packages, setup

setup(
    name='django-envconfig',
    packages=find_packages(exclude=['tests']),
    version='0.1.0',
    license='MIT',
    description='Configure Django using environment variables.',
    author='Elyas Khan',
    author_email='mail@ely.as',
    url='https://github.com/ely-as/django-envconfig',
    keywords=[],
    install_requires=[
        'Django',
        'python-dotenv',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Typing :: Typed',
    ],
)
