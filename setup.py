import setuptools

long_description = open('README.rst').read()

setup_params = dict(
    name='CacheControl',
    version='0.5',
    author='Eric Larson',
    author_email='eric@ionrock.org',
    license='MIT',
    url='https://github/ionrock/cachecontrol',
    keywords='requests http caching web',
    packages=setuptools.find_packages(),
    description='httplib2 caching for requests',
    long_description=long_description,
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)