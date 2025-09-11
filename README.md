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

### Project goals

- [x] Add basic routes for characters, houses and organisations
- [x] Implement pagination on all endpoints
- [x] Add some other fun routes for additional information, e.g. `GET /character/random`
- [ ] Add a route and validation for getting a single character
- [ ] Add all seed data for basic routes
