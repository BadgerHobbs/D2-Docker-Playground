# D2-Docker-Playground

Simple playground for [diagramming scripting language D2](https://github.com/terrastruct/d2) running in Python and optionally Docker.

![image](https://user-images.githubusercontent.com/23462440/204005280-42357ab8-4772-47a1-93d7-3550660f1673.png)

## Running in Python

Run the python program from the main directory
```bash
python3 api.py
```

Access in browser at http://localhost:5000/

## Running in Docker

Build the image from the main directory
```bash
docker build -t d2-playground .
```

Run the container
```bash
docker run -d \
    --name d2-playground \
    -p 5000:5000 \
    --restart on-failure \
    d2-playground
```
