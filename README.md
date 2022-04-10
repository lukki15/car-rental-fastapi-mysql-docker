# Car Rental

setup based on https://github.com/cymagix/fastapi-mysql-docker

- FastAPI
- MySQL
- Docker

## Setup

Please install `Docker` and `Docker compose` first.

https://www.docker.com/

After installation, run the following command to create a local Docker container.

```bash
docker-compose build
docker-compose up -d
```

If you want to check the log while Docker container is running, then try to use following command:

```bash
docker-compose up
```

If Docker is running successfully, the API and DB server will be launched as shown in the following:

- API server: http://localhost:8000
- DB server: http://localhost:3306

*Be careful, it won't work if the port is occupied by another application.*

A summary of all end-points ca be seen in the Swagger UI under
- FastAPI - Swagger UI : http://localhost:8000/docs

For shutdown of the docker instance, please use following command:

```bash
docker-compose down
```

