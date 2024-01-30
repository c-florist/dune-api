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

### Project goals

- [x] Add basic routes for characters, houses and organisations
- [ ] Add all seed data for basic routes
- [ ] Add some other fun routes for additional information, e.g. `GET /characters/random`
- [ ] Add CI/CD pipeline and make deployable on AWS (or other free tier cloud service)
