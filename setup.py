name = 'loopyng'
root_url = 'https://github.com/thorwhalen'

# version = '0.0.1'

more_setup_kwargs = dict(
    install_requires=[
        'numpy',
        'matplotlib',
        'pysoundfile'
    ],
    description="Tools for audio generation and transformation.",
    keywords=['data', 'signal processing', 'audio'],
    author='Thor Whalen',
    license='Apache Software License',
    # download_url='{root_url}/{name}/archive/v{version}.zip'),
)

from pip_packaging import next_version_for_package
from setuptools import setup

import os

# name = os.path.split(os.path.dirname(__file__))[-1]

version = next_version_for_package(name)
print(f"---> Next pypi version for {name}: {version}")


def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except:
        return ""


ujoin = lambda *args: '/'.join(args)

if root_url.endswith('/'):
    root_url = root_url[:-1]


def my_setup(print_params=True, **setup_kwargs):
    from setuptools import setup
    if print_params:
        import json
        print("Setup params -------------------------------------------------------")
        print(json.dumps(setup_kwargs, indent=2))
        print("--------------------------------------------------------------------")
    setup(**setup_kwargs)


dflt_kwargs = dict(
    name=f"{name}",
    version=f'{version}',
    url=f"{root_url}/{name}",
    include_package_data=True,
    platforms='any',
    long_description=readme(),
    long_description_content_type="text/markdown",

)

setup_kwargs = dict(dflt_kwargs, **more_setup_kwargs)

my_setup(**setup_kwargs)
