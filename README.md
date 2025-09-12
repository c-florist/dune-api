# dune-api

An API that provides information about the world of Dune, the book series created by Frank Herbert.

The focus for this API is the original book series, so it doesn't include any information added afterwards, for example in the prequels.

## Development

### Prerequisites
This project uses:
1. [mise](https://mise.jdx.dev/getting-started.html) for dev environment management and task running.
1. [uv](https://github.com/astral-sh/uv) for python package management.

### Setup
For a development install, clone the repository and initialise your virtual environment:
```shell
git clone https://github.com/kyoh-dev/dune-api.git

cd dune-api

uv sync
```

Check the mise.toml for helpful scripts under "tasks", otherwise you can run the below to start the dev server:
```shell
source .venv/bin/activate
uvicorn app.main:app --reload
```
