git clone https://github.com/digsci/floodwork.git  
cd floodwork  
mkdir -p data/toLoad  
Copy datafiles to ${PWD}/data/toLoad  
docker run --network=bridge_network --name flood-db -p 8890:8890 -p 1111:1111 -v ${PWD}/data:/data -e DBA_PASSWORD=dba -e SPARQL_UPDATE=true -d graham/virtuoso-db:1.0  
(Database might take some time to load data - UI available at localhost:8890)  
docker run --network=bridge_network --name notebook -p 8888:8888 -v ${PWD}:/home/jovyan graham/jupyter-notebook-jba:1.0  

