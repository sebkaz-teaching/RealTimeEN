---
layout: page
title: Docker
---

All the necessary programs will be delivered in the form of docker containers.

## Start with Docker

In order to download the docer software to your system, go to [ the page](https://docs.docker.com/get-docker/).

If everything is installed correctly, follow these instructions:

1. Check the installed version

```{bash}
docker --version
```

2. Download and run the image `Hello World` and

```{bash}
docker run hello-world
```

3. Overview of downloaded images:

```{bash}
docker image ls

docker images
```

4. Overview of running containers:

```{bash}
docker ps 

docker ps -all
```

5. Stopping a running container: 

```{bash}
docker stop <CONTAINER ID>
```

6. Container removal
```{bash}
docker rm -f <CONTAINER ID>
```

I also recommend [short intro](https://medium.com/codingthesmartway-com-blog/docker-beginners-guide-part-1-images-containers-6f3507fffc98)


## Docker as an application continuation tool

[Docker with jupyter notebook](https://hub.docker.com/repository/docker/sebkaz/docker-data-science)
