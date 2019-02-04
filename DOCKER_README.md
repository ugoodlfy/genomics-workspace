1. Download docker for windows: https://www.docker.com/docker-windows 
2. Download docker for mac :https://hub.docker.com/editions/community/docker-ce-desktop-mac
3. After installing, go to settings to check feature of sharing drive is activated
4. Introduce some important and common commend to manipulate docker:
   check the current images:
       ```docker images```
   check all containers (include all of status):
       ```docker ps -a``` 
   remove docker image:
       ```docker rmi [imageID]```
   build and run docker container from image:
       ```docker run [option] imageID```
   remove docker container:
       ```docker rm [containerID]```
   execute container:
       ```docker exec -it [containerID] bash```
5. use Dockerfile to make customize image:
       some commend will be used in Dockerfile:
           1.FROM
           2.COPY
           3.ADD
           4.ENV
           5.CMD
           6.RUN
           7.WORKDIR 
    link to the websire to learn more detail for Dockerfile : https://docs.docker.com/engine/reference/builder/
6. After completing Dockerfile use ```docker build . ``` to build the image
7. To run multiple-container docker application docker-compose is a good tool to acheive it 
   1. Make sure you have already installed both Docker Engine and Docker Compose. You don’t need to install Python or Redis, as both are provided by Docker images.
   2. Create a Dockerfile
   3. Define services in a compose file (docker-compose.yml)
   4. run ```docker-compose up```
8. Example for Dockerfile:
     ```
     FROM python:3.4-alpine
     ADD . /code
     WORKDIR /code
     RUN pip install -r requirements.txt
     CMD ["python", "app.py"]
     ```
9. Example for docker-compose.yml
     ```
     version: '3'
     services:
      web:
       build: .
       ports:
        - "5000:5000"
       volumes:
        - .:/code
      redis:
       image: "redis:alpine"
       ```