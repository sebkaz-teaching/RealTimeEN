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


The easiest way how to run JupyterLab with your new python env. For _<name of Your env>_ You can choos what You want. 

```bash
python3 -m venv <name of Your env>

source <name of your env>/bin/activate
# . env/bin/activate
pip install --no-cache --upgrade pip setuptools

pip install jupyterlab numpy pandas matplotlib scipy
# or
pip install -r requirements.txt

jupyterlab
```
go to web browser: _localhost:8888_

If You want rerun jupyterlab (after comupter reset) just go to Your folder and run: 

```bash
source <name of your env>/bin/activate
jupyterlab
```


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
