Poetry-demo
============

Basic repository exploring poetry for packaging

To install this repo
----------------------

- Create a virtual environment (conda or otherwise)

- Install poetry into virtual environment

- (Activate environment)

- `poetry install`

- `python -m pip install -e .`


To use poetry on your own
-------------------------

- Create a virtual environment (conda or otherwise)

- Install poetry into virtual environment

- (Activate environment)

- `poetry add <packages you need>`

- `poetry lock` to pin versions

- `poetry build` to package source distribution and wheel

Mixing and matching conda and poetry
----------------------------------------

It looks like you can use poetry commands to install packages into a conda environment, but you cannot use conda to install packages and expect poetry to update the lockfile/toml file accordingly.
The least painful method of converting a conda yaml file may be to `poetry add <package` one at a time from a bare python environment that only contains poetry, then letting poetry resolve dependencies, updating the toml/lockfiles along the way.
Some cryptic error messages when using pip to install a package locally
