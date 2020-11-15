from setuptools import find_packages, setup


setup(
    name='cmn',
    version='0.0.1',
    url='http://example.com',
    description='Test exercise to calculate a math problem',
    # long_description=LONG_DESC,
    author='Pynchia', author_email='pyncha@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'],
    keywords=['dmo', ],
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    runme = cmn.cli:cli
    """,
    install_requires=[]
)
