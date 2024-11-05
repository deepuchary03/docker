
# Docker Commands

To execute Docker commands, use the following commands in your terminal:

```bash
git clone https://github.com/deepuchary03/docker
cd docker

```
```bash
docker --version          # To verify Docker is installed and to know the version

docker ps                 # To check the current running containers

docker ps -a              # To check all the containers (including stopped containers)

docker build -t simple-flask-app .  # To build a container named simple-flask-app

docker run simple-flask-app  # To run the simple-flask-app container

docker images             # To list all the images
```
