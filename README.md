# language-detection-api

API for detecting language of an input text

## How to setup

Create a new venv (virtual environment):

```bash
python3 -m venv .venv
```

Activate new environment:

For Mac/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
source .venv/Scripts/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

## Run the server

```bash
uvicorn main:app --reload
```

The server is running on [http://localhost:8000](http://127.0.0.1:8000/). Swagger documentation can be accessed at [http://localhost:8000/docs](http://127.0.0.1:8000/docs).

To send a request via your terminal, paste & run the following command:

```bash
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' http://localhost:8000
```

---

## How to build & run the Docker Image

```bash
docker build -t language-detection-api .
```

Run the Docker Image with:

```bash
docker run -d --rm -p 8000:8000 --name language-detection-api language-detection-api
```

You can now access the api at [http://localhost:8000](http://127.0.0.1:8000/). Swagger documentation are available at [http://localhost:8000/docs](http://127.0.0.1:8000/docs).

<br/>

To view the logs of the container run:

```bash
docker logs language-detection-api
```

To stop the container run:

```bash
docker stop language-detection-api
```
