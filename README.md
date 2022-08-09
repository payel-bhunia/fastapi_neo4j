#Containerize FastAPI application with neo4j

Recently, I had difficulties to containerize my FastAPI application which use neo4j database to store and retrieve data. And so, I thought to create this application to help people save their time from trying to figure out how to do it.


It is considered to be a best practice that a container should have only one process and single responsibility. But as I am going to dockerize Python based FastAPI app and neo4j graph database for storing data for the app, so I need two containers – one for running the app and another one for running the Neo4j database.


So you need docker compose file for these two containers to run independently and to establish communication between them.
Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Using Compose is basically a three-step process:

1. Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
2. Define the services in docker-compose.yml so they can be run together in an isolated environment.
3. Run docker-compose up to start and run your entire app.

I will show you how to do a basic setup on the neo4j inside the container so you can start connecting to it from your Python application. 
