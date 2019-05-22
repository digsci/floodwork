DEPENDENCIES  
Docker images:  
docker load < jupyter-notebook-jba.tar.gz  
docker load < virtuoso-db.tar.gz  
Data:  
flood-data.tgz  


INSTALL / RUN  
git clone https://github.com/digsci/floodwork.git  
cd floodwork   
mkdir data   
cd data  
tar xvf flood-data.tgz  
cd ..  
docker-compose up  
Jupyter notebook at: 127.0.0.1:8888/  
docker-compose down  
