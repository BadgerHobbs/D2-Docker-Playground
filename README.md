# D2-Docker-Playground

Simple playground for [diagramming scripting language D2](https://github.com/terrastruct/d2) running in Python and optionally Docker.

![image](https://user-images.githubusercontent.com/23462440/204071887-62c9b276-444d-49b0-a2b8-5ea72cb09c88.png)

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
