# EastVantage Python Assessment

### Pre-Requisite
- Python 3
- Docker (optional)

### Setup Instructions (venv)

1. Setup the virtual environment
`python -m venv`
2. Run the virtual environment
`source venv/bin/activate`
3. Run the backend
`uvicorn app.main:app --reload`
4. You can now access the API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Setup Instructions (docker)

Run these commands from the project root.

1. Build the image
`docker build -t ev-fastapi .`
2. Run the container
`docker run --rm -p 8000:8000 ev-fastapi`
3. You can now access the API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

The SQLite database is created inside the container, so data is lost when the container stops.

### Running the Unit Tests

#### With pytest (venv)

1. Activate the virtual environment
`source venv/bin/activate`
2. Run the tests from the project root
`pytest`

#### With docker

1. Build the image (skip if already built)
`docker build -t ev-fastapi .`
2. Run the tests inside the container
`docker run --rm ev-fastapi pytest`