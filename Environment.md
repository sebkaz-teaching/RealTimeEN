---
layout: page
title: Environment
---

## Python env with Jupyter LAB

For our first a few laboratories we will use just python codes. 
Check what is Your Python3 environment. 

In the terminal try first:
```bash
python
# and
python3
```

I have python3 (You shouldn't use python 2.7 version) so i get new and clear python environment.


The easiest way how to run JupyterLab with your new python env. 
For _<name of Your env>_ You can choose what You want. 

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

If You want rerun jupyterlab (after computer reset) just go to Your folder and run: 

```bash
source <name of your env>/bin/activate
jupyterlab
```


## Python env with JupyterLAB Docker Version

### Cookiecutter project 
From [GitHub](https://github.com/sebkaz/jupyterlab-project) repository You can
find how to use a cookiecutter for any data science project or other kind of programs. 

To run and build full dockerfile project:
Create python env and install cookiecutter library.
```bash
python3 -m venv venv
source venv/bin/activate
pip --no-cache install --upgrade pip setuptools
pip install cookiecutter
```
and run:
```bash
cookiecutter https://github.com/sebkaz/jupyterlab-project
```
You can run a cookiecutter project directly from GitHub repo.

Answer questions: 
```bash
cd jupyterlab
docker-compose up -d --build
```
To stop: 
```bash
docker-compose down
```

### Cookiecutter with config yaml file

1. [Python, Julia, R](https://github.com/sebkaz/docker-jupyterlab)
2. [All + Apache Spark](https://github.com/sebkaz/docker-spark-jupyterlab)

Clone repo and run:
```bash 
python3 -m cookiecutter https://github.com/sebkaz/jupyterlab-project --no-input --config-file=spark_template.yml --overwrite-if-exists
```

## Older Docker version with Jupyter notebook

#### From GitHub repository
Take Dockerfile from [Git](https://github.com/sebkaz/docker-data-science) repository and run:

```bash
docker build -t docker-data-science

docker run -d -p 8888:8888 docker-data-science
```

#### From Docker Hub repository
You can also run this image from DockerHub repo:
```bash
docker run -d -p 8888:8888 sebkaz/docker-data-science
```

After docker run go to _http://localhost:8888_

PASS: root

>> !REMEMBER - I don't use -v (_volume_) option so You must save Your works all the time.

## Older version with SPARK in Jupyter notebook

#### From GitHub repository
Take Dockerfile from [GitHub](https://github.com/sebkaz/docker-spark-jupyter) repository and build the image:
```bash
docker build -t docker-spark-jupyter
```
After that You can run it with:
```bash
docker run -d -p 8888:8888 docker-spark-jupyter
```

#### From Docker Hub repository
You can also run this image from DockerHub repo:
```bash
docker run -d -p 8888:8888 sebkaz/docker-spark-jupyter
```

After docker run: go to _http://localhost:8888_

PASS: root

>> REMEMBER - I don't use -v (_volume_) option, so You must save Your works all the time.


## Apache AIRFLOW - local mode 

```bash
mkdir airflow-local
cd airflow-local

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.0/dockert-compose.yaml'

mkdir ./dags ./logs ./plugins

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

cat .env
```


first run
```bash
docker-compose up airflow-init
```

To run env 
```bash
docker-compose up -d --build
```

Web browser
```
localhost:8080
```

to stop 
```
docker-compose down --volumes --rmi all
```