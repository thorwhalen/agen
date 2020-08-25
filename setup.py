version = '0.0.1'
root_url = 'https://github.com/thorwhalen'
name = 'loopyng'

import os
from pip_packaging import format_str_vals_of_dict, next_version_for_package
from setuptools import setup


# name = os.path.split(os.path.dirname(__file__))[-1]


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

    author='Thor Whalen',
    license='Apache Software License',

    include_package_data=True,
    platforms='any',
    long_description=readme(),
    long_description_content_type="text/markdown",

)

# setup_kwargs = format_str_vals_of_dict(dflt_kwargs, name=name, root_url=root_url, version=version)
setup_kwargs = dflt_kwargs

more_setup_kwargs = dict(
    install_requires=[
        'numpy',
        'matplotlib',
        'pysoundfile'
    ],
    description="Tools for audio generation and transformation.",
    keywords=['data', 'signal processing', 'audio'],
    # download_url='{root_url}/{name}/archive/v{version}.zip'),
)

setup_kwargs = dict(setup_kwargs, **more_setup_kwargs)

my_setup(**setup_kwargs)
