# project_template

I'm working with a lot of git repositories and here is my current favorite setup.

## uv setup

```
uv init
uv venv --python 3.13
source .venv/bin/activate
```

## favorite modules

```
uv add ipykernel
uv add python-dotenv
uv add loguru

uv add matplotlib
uv add pandas
uv add scikit-learn

uv add streamlit

uv add pytest
```

## start script

```sh
. ./scripts/setup.sh
```