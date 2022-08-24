#Deploy FastAPI application & neo4j database in openshift

In my previous post I had shown how to containerize FastAPI application which uses neo4j database to store and retrieve data

Here I have created a basic application which stores person details (name and age) into neo4j database and fetch those information from the database. I have one Dockerfile which I will use to deploy in Openshift.

Prerequisite: Neo4j already deployed on openshift and externally can be accessible

I have already deployed neo4j service on openshift. If you haven't yet you can follow my post to deploy neo4j on openshift or you can use local to build your application temporarily.

