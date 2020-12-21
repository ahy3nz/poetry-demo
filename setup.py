# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_demo']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.4,<2.0.0',
 'pandas>=1.1.5,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'scikit-learn>=0.23.2,<0.24.0']

setup_kwargs = {
    'name': 'poetry-demo',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alex Yang',
    'author_email': 'ayang41@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
