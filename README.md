# osdu-tutorials-python
OSDU tutorials for various use cases in Python

# QuickStart web app
Simple web application demonstrating how to use Authentication, Search and Delivery APIs

## Before you start
1. Get client ID, client Secret, Authorization URL and API URL from your platform admin.
2. Clone this repository.
3. Go to 'quickstart' folder, rename default environment file to config-azure|aws|gcp.env and fill out the values:
```
# OAuth settings
OSDU_CLIENT_ID=<your-client-id>
OSDU_CLIENT_SECRET=<your-client-secret>
OSDU_AUTH_BASE_URL=<auth-server-url>

# API
OSDU_API_BASE_URL=<api-base-url>
```

## How to run locally in WSL/Linux

1. Download and install Python.
2. Create and activate virtual environment:
```
$ python3 -m venv --prompt quickstart .venv/quickstart
$ source .venv/quickstart/bin/activate
```
3. Install required packages:
```
$ pip install -r requirements.txt
```
4. Export environment variables:

For Azure
```
$ export $(grep -v '^#' config-azure.env | xargs -d '\n')
```
For AWS
```
$ export $(grep -v '^#' config-aws.env | xargs -d '\n')
```
5. Run the server in quickstart/src folder:
```
$ cd src
$ gunicorn entry_api:api -b 0.0.0.0:8080
```
6. Go to http://localhost:8080

## How to run inside Docker container

1. Edit docker-compose.yml to include configuration to your environment:
```
version : '3'
services:
  backend:
    env_file:
      - config-<your-env>.env
    build: .
    ports:
      - "8080:8080"
    command: gunicorn entry_api:api -b 0.0.0.0:8080
```
2. Build the image and run the container:
```
$ docker-compose up --build
```
3. Go to http://localhost:8080