git clone https://github.com/digsci/floodwork.git  
cd floodwork  
mkdir -p data/toLoad  
Copy datafiles to ${PWD}/data/toLoad  
docker-compose up
Jupyter notebook at: 127.0.0.1:8888/?token=<token id genersted by jupyter notebook startup>
docker-compose down
