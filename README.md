# Anaconda
- Create a environment with Python 3.9.13
- Activate the environment

# FastAPI Exercise 1
- Navigate to folder `fastapi-1`
- Download the packages required: `FastAPI` and `Uvicorn` server
  - [FastAPI](https://fastapi.tiangolo.com/#installation)
  - [Uvicorn](https://www.uvicorn.org/#quickstart)
- Run the server
```
uvicorn main:app --reload
```
- Check out the API at `localhost:8000/docs`
# FastAPI Exercise 2
- Navigate to folder `fastapi-2`
- Download another package: `Jinja`
  - [Jinja](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation)
- Run the server
```
uvicorn main:app --reload
```
- Check out the API at `localhost:8000/docs`
- We also have a rendered template at `localhost:8000/index` for a quick preview of how the API work on a full-fledged web site.

# FastAPI Exercise 3
- Navigate to folder `fastapi-3`
- Download the packages for YOLOv5 model with the `requirements.txt`
- Run the server
```
uvicorn main:app --reload
```
- Check out the new API at `localhost:8000/docs`
- Try sending an image in the `test-images` folder to the API at `/image2image` and see what happens.
# Docker Exercise 1
- Pull the image `qdgiang/seminar-ex1`
- Run the image **in detached mode**
- Exec inside the image with the command `/bin/sh`
- Read the content of the file `hello.txt` there
- Exit from inside the container
- Stop the running container
- Delete the stopped container
# Docker Exercise 2
- Pull the image `qdgiang/seminar-ex2`
- Run the image **in foreground mode**, and read what is printed on the terminal
- Can you change the environment variable with an updated `docker run` command this time?
# Docker Exercise 3
- Navigate to the folder `fastapi-1`
- Update the Dockerfile to build the image for the server
- Build the image using `docker build` command. Remember to set your own name for the image using the `-t` flag
- Run your build image in detached mode. Remember to **map the port** from your computer to inside your container using the `-p` flag. Hint: The FastAPI server **inside the container** is opened at port `8000`
- Check out the API at `localhost:PORT_THAT_YOU_JUST_MAP/docs`. If you can see the UI, congrats!
# Docker Exercise 4


