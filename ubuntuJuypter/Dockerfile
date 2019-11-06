#FROM ubuntu:latest
FROM debian:latest 

RUN apt-get update && \
    apt-get install -y python3-pip


RUN pip3 install --upgrade pip
RUN pip3 install tensorflow \
    tensorflow-object-detection-api \
    jupyter notebook \
    jupyterlab \
    nltk \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    setuptools \
    keras \
    tqdm \
    nodejs \
    pyQts \
    scrapy \
    gensim 


EXPOSE 8888

RUN mkdir tf_log
RUN useradd -ms /bin/bash jupyter

WORKDIR /home/jupyter

RUN chown -R jupyter:jupyter /home/jupyterlab
RUN chmod 755 /home/jupyterlab

USER jupyter

ENTRYPOINT ["jupyter", "lab", "--no-browser", "--ip=*", "--NotebookApp.password=''", "--NotebookApp.token=''"  ]



