docker run --network=bridge_network --name flood-db -p 8890:8890 -p 1111:1111 -v ${PWD}/data:/data -e DBA_PASSWORD=dba -e SPARQL_UPDATE=true -d graham/virtuoso-db:0.3
docker run --network=bridge_network --name notebook -p 8888:8888 -v ${PWD}:/home/jovyan graham/jupyter-notebook-jba:0.2

