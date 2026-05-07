# HERMES - Template

Support namespace package template to interface a new device or algorithm in [HERMES](https://github.com/maximyudayev/hermes).

## Installation
Provide additional installation requirements (e.g. any OEM SDK, settings in a 3rd party app, etc.).

### From PyPI
```bash
pip install pysio-hermes-<pkg_name>
```

### From source
```bash
git clone https://github.com/maximyudayev/hermes-<pkg_name>.git
pip install -e hermes-<pkg_name>
```

## Usage
Using the device/algorithm follows the standard [configuration file specification](https://yudayev.com/hermes) process of HERMES nodes.

## Building
Building and releasing packages is easy with [UV](https://docs.astral.sh/uv/getting-started/installation/). Install git-changelog to auto-generate release notes from commit history: `uv tool install git-changelog ruff`.

1. Run auto-formatter: `ruff format .`
1. Commit all changes for the next release
1. Bump the package version with UV: `uv version --bump <[major,minor,patch]>`
1. Use the new version number to update the CHANGELOG.md: `git-changelog --bump <above_version> -c angular -s :all:`
1. Commit the updates as: `git commit -m "release: v<above_version>"`
1. Tag the release commit: `git tag <above_version>`
1. Build the package: `uv build`
1. Publish on PyPi: `uv publish --token <your_pypi_token>`

## Citation
When using any parts of this repository outside of its intended use, please cite the parent project [HERMES](https://github.com/maximyudayev/hermes).
