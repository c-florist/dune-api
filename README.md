# dune-api

An API that provides information about the world of Dune, the book series created by Frank Herbert.

The focus for this API is the original book series, so it doesn't include any information added afterwards, for example in the prequels.

## Development

### Prerequisites

1. This project uses [mise](https://mise.jdx.dev/getting-started.html) for dev environment management.
1. This project uses [uv](https://github.com/astral-sh/uv) for python package management.

### Setup
For a development install, clone the repository and initialise your virtual environment:
```shell
git clone https://github.com/kyoh-dev/dune-api.git

cd dune-api

uv sync
```

### TODO

- [ ] Add a route and validation for getting a single character
- [ ] Add a planet model and table, with associated get / getall routes
- [ ] Add an endpoint to accept a lat/lon, identify where the user is and return the most similar planet based on environment (e.g. desert, island, ocean, forest)
