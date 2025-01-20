# APILOG

This project is a simple API logging tool that logs API responses to a MongoDB database.

It also provides a script to save the data from MongoDB to CSV and PARQUET files.

## Citybikes API
[Citybikes](https://citybik.es/) API is a public API that provides real-time information about bike sharing systems in various cities around the world. This project uses this API to log data and save it for further analysis.

This project only usus [Citybikes API](https://api.citybik.es/v2/) to get data of the city of Coruña.

## Installation
1. Clone this repository
2. Install dependencies using pip: `pip install -r requirements-full.txt`

This requirements file includes all dependencies required for both scripts and also for running jupyter notebooks.

## Usage

### Environment variables
- MONGO_URL: identifies the mongo database url
- INTERVAL: especify the interval between api queries (default is 120 seconds)

### Run

- To log API responses, run the script directly with:   
```bash 
$ MONGO_URL='mongodb://localhost:27017/' INTERVAL=120 python apilog/apilog.py
```
- To save data from MongoDB to CSV and PARQUET files, run the script:
```bash 
$ MONGO_URL='mongodb://localhost:27017/' python apilog/apisave.py
```
You can also use your Mongo Atlas account just changing the MONGO_URL variable, for example:

```bash 
$ export MONGO_URL='mongodb+srv://<your-username>:<your_password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
$ python apilog/apisave.py
```

## Apilog Docker Image

The docker image for the apilog script is available in Docker Hub, [here](https://hub.docker.com/u/bigdatawirtz). 

### Run

Don't forget the MONGO_URL and INTERVAL environments variables when creating the apilog docker.

`docker run -e INTERVAL=120 -e MONGO_URL='mongodb+srv://<your-username>:<your_password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' bigdatawirtz/apilog `

You can also create the docker image from code using Dockerfile in this repository with the following command:
`docker build -t apilog . `


### Run with Docker-compose

You can crete your own infrastructure with two containers: one for the logger and other one for mongo database. Use the docker-compose.yml file in this repo:

`docker compose up -d`