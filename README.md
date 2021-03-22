# falcon-docker
Minimal Docker image for Falcon Framework Python3 app on Alpine Linux

Run with:
```
docker-compose build
docker-compose up -d
```


## How to use this image

We assume your application code is in the directory `src` and your *Falcon* entrypoint is the `app` object in `src/main.py`.

```
.
├── LICENSE
├── README.md
├── docker-compose.yaml
├── service1
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src
│       └── main.py
└── service2
    ├── Dockerfile
    ├── requirements.txt
    └── src
        └── main.py
```
