FROM jupyter/scipy-notebook:latest
ADD jupyter_notebook_config.py /home/jovyan/.jupyter/
RUN conda install -y -c conda-forge sparqlwrapper
RUN conda install -c conda-forge folium
RUN pip install sparqlkernel
USER jovyan 
RUN jupyter sparqlkernel install --user
