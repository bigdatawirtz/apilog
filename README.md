# APILOG


## Environment variables
- MONGO_URL: identifies the mongo database url
- INTERVAL: especify the interval between api queries (default is 120 seconds)

Run the script directly with:
```bash 
$ MONGO_URL='mongodb://localhost:27017/' INTERVAL=20 python apilog/apilog.py
```
