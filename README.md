# project_template

Here is my current favorite setup of a Python based project in vscode.

To get started:

1. clone repo
2. run `uv sync`
3. run `make test`
4. run `make`

## Usage

- `make` or `make help`: show help
- `make test`: run tests
- `make say MSG="Hello"`: run app's subcommand `say` with argument
- `make shout MSG="Hello"`: run app's subcommand `shout` with argument
- `make repeat MSG="Hello" TIMES=3`: run app's subcommand `say` with argument


## Detail

I'm using [uv](https://docs.astral.sh/uv/) as the package manager.

The following modules are setup:

- `ipykernel` - vscode only needs the kernel not the full-fledged Jupyter server
- `python-dotenv` - load environmental variables from `.env` file
- `pytest`

- `loguru` - for logging

- various data engineer/science modules: `matplotlib`, `pandas`, `scikit-learn`, and `streamlit`
