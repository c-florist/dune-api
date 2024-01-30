# dune-api

An API that provides information about the world of Dune, the book series created by Frank Herbert.

The focus for this API is the original book series, so it doesn't include any information added afterwards, for example in the prequels.

## Development

For a development install, clone the repository and install with extra dev/test dependencies:
```shell
git clone https://github.com/kyoh-dev/dune-api.git

cd dune-api

pip install -r requirements.txt -r requirements.dev.txt
```

### Makefile targets
```shell
# Start local development server
make start

# Initialise test database and seed data
make init-tests

# Run test suite
make test

# Run linting tools
make lint-check
make lint-fix
```

### Project goals

- [x] Add basic routes for characters, houses and organisations
- [x] Implement pagination on all endpoints
- [x] Add some other fun routes for additional information, e.g. `GET /character/random`
- [ ] Add a route and validation for getting a single character
- [ ] Add all seed data for basic routes

### Data to add

- [ ] Planets
