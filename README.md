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

If you want to check docker is actually working, then you can check it with following command:

```bash
docker ps
```

If you want to go inside of docker container, then try to use following command:

```bash
docker-compose exec mysql bash
docker-compose exec api bash
```

For shutdown of the docker instance, please use following command:

```bash
docker-compose down
```