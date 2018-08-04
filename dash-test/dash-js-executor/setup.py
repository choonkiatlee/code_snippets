from setuptools import setup

exec (open('dash_js_executor/version.py').read())

setup(
    name='dash_js_executor',
    version=__version__,
    author='choonkiatlee',
    packages=['dash_js_executor'],
    include_package_data=True,
    license='MIT',
    description='Executes arbritary javascript / HTML within dash',
    install_requires=[]
)
