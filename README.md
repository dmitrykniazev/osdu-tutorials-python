# osdu-tutorials-python
OSDU tutorials for various use cases in Python

# Starting container

```
docker-compose up --build
```

# Starting server in VSCode Remote-containers env

```
cd /workspace/quickstart && gunicorn entry_api:api -b 9000 --reload
```
