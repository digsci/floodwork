**Flood Risk Management**

A set of Jupyter notebooks and associated technologies used to demonstrate flexible integrated querying of flood risk data.

***Dependencies***
  
Requires the flood risk data - flood-data.tgz  

***To install*** 
 
~~~~
git clone https://github.com/digsci/floodwork.git  
cd floodwork   
mkdir data   
cd data  
tar xvf flood-data.tgz  
cd ..  
~~~~

***To run***

~~~~
docker-compose up    
[Jupyter notebook at: 127.0.0.1:8888/]
docker-compose down  
~~~~

***Note:*** The Virtuoso database can take some time to start as it needs to load the data.  It can be checked at `localhost:8890` where eventually a full UI will appear.
