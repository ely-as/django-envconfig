from pathlib import Path

from setuptools import find_packages, setup

with open(Path(__file__).parent / 'README.md') as f:
    long_description = f.read()

setup(
    name='django-envconfig',
    packages=find_packages(exclude=['tests']),
    version='0.2.3',
    license='MIT',
    description='Configure Django using environment variables.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Elyas Khan',
    author_email='mail@ely.as',
    url='https://github.com/ely-as/django-envconfig',
    project_urls={
        'Source': 'https://github.com/ely-as/django-envconfig',
        'Tracker': 'https://github.com/ely-as/django-envconfig/issues',
    },
    keywords=[],
    install_requires=[
        'Django',
        'python-dotenv',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Typing :: Typed',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
    ],
)
