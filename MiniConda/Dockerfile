FROM continuumio/miniconda3

RUN conda create -n env python=3.6 && \
    conda install -y git \
                numpy \
                jupyterlab \
                pandas \
                matplotlib \
                seaborn \
                scikit-learn \
                setuptools \
                keras \
                tqdm \
                nodejs \
                scrapy \
                gensim \
                tensorflow && \
                pip install --upgrade pip && \
                pip install nltk \
                            gym \
                            ggplot \
                            pyqt5 \
                            pyopengl \
                pip --upgrade tensorflow && \
                conda install -y -c conda-forge pycocotools

EXPOSE 8888

RUN echo "source active env " > ~/.bash
ENV PATH /opt/conda/envs/env/bin:$PATH
# Update conda
RUN conda update -y conda 

RUN pip3 install Pillow \
        tensorflow-object-detection-api
        
# Working dir for jupyter
RUN mkdir workspace \
         models

#install all tenserflow models
# add '-c http.sslVerify=false' to  bypass http
RUN git clone --depth 1 https://github.com/tensorflow/models && \
        pwd && \
        cd /models/research && \
        pip install .

# run jupyter note book

ENTRYPOINT [ "jupyter", "lab", "--notebook-dir=./workspace", "--no-browser", "--ip=*", "--Notebook.password=''", "--notebook.token=''", "--allow-root" ]

