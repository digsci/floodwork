# Run Virtuoso docker container

docker run --name flood-db -p 8890:8890 -p 1111:1111 -v ${PWD}/data:/data -e DBA_PASSWORD=dba -e SPARQL_UPDATE=true -d tenforce/virtuoso
docker exec -it flood-db /bin/bash
isql-v localhost dba dba load_gauge_graph
isql-v localhost dba dba load_property_graph
exit
cd ..
jupyter notebook
