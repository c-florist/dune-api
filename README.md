# dune-api

An API that provides information about the world of Dune, the book series created by Frank Herbert.

The focus for this API is the original book series, so it doesn't include any information added afterwards, for example in the prequels.

## Development

### Prerequisites
This project uses:
1. [mise](https://mise.jdx.dev/getting-started.html) for dev environment management and task running.
1. [uv](https://github.com/astral-sh/uv) for python package management.

It's recommended to use mise as it will automatically use your python venv.

### Setup
For a development install, clone the repository and initialise your virtual environment:
```shell
git clone https://github.com/kyoh-dev/dune-api.git
cd dune-api

# Initialise your dev environment
mise run init
# or
uv sync && python -m scripts.seed_database

# Run the dev server with
mise run dev
# or
source .venv/bin/activate
uvicorn app.main:app --reload
```

Check the mise.toml for other helpful scripts under "tasks".
