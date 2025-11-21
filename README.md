# project_template

I'm working with a lot of git repositories and here is my current favorite setup.

## uv setup

```
uv init
uv venv --python 3.13
source .venv/bin/activate

uv add ipykernel
uv add streamlit
uv add python-dotenv
uv add loguru
```

## start script

```sh
. ./scripts/setup.sh
```