# Sample FastAPI App

This is a sample FastAPI app that demonstrates how to create a simple API using FastAPI.

## Setup & Installation

1. Clone the repository

```bash
git clone
```

2. Change the directory

```bash
cd helloworld_fastapi
```

3. Create Conda environment with Python 3.12

```bash
conda create -n hello_fastapi python=3.12
```

4. Activate the environment

```bash
conda activate hello_fastapi
```

5. Install the requirements

```bash
conda install -c conda-forge fastapi uvicorn -y
```

## Running the app

Run the following command to start the app

```bash
uvicorn main:app --reload
```
## API Endpoints
localhost:8000/docs - Swagger UI
localhost:8000/redoc - ReDoc UI 
