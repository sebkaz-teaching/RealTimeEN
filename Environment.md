---
layout: page
title: Environment
---


## Python env with Jupyter LAB
In the terminal try first:
```bash
python
# and
python3
```

I have python3 (You should't get python 2.7 version) so i get new and clear env.

```bash
python3 -m venv env

source env/bin/activate
# . env/bin/activate
pip install --no-cache --update pip setuptools

pip install jupyterlab numpy pandas matplotlib scipy

jupyterlab
```
go to web browser: _localhost:8888_

## Python env with Jupyter LAB Docker Version


## Older Docker version with Jupyter notebook

#### From GIT hub repository
[Git](https://github.com/sebkaz/docker-data-science)

```bash
docker build -t docker-data-science

docker run -d -p 8888:8888 docker-data-science
```

#### From Docker Hub repository

```bash
docker run -d -p 8888:8888 sebkaz/docker-data-science
```

After docker run: go to _http://localhost:8888_

PASS: root

>> !REMEMBER - I don't use -v (_volume_) option so You must save Your works all the time.

## Older version with SPARK in Jupyter notebook

#### From GIT hub repository
[Git](https://github.com/sebkaz/docker-spark-jupyter)

```bash
docker build -t docker-spark-jupyter

docker run -d -p 8888:8888 docker-spark-jupyter
```

#### From Docker Hub repository

```bash
docker run -d -p 8888:8888 sebkaz/docker-spark-jupyter
```

After docker run: go to _http://localhost:8888_

PASS: root

>> !REMEMBER - I don't use -v (_volume_) option so You must save Your works all the time.
