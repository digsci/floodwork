DEPENDENCIES  
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
The Virtuoso database can take some time to start as it needs to load the data.  
It can be checked at localhost:8890 where enventually a full UI will appear.  
Jupyter notebook at: 127.0.0.1:8888/  
docker-compose down  
