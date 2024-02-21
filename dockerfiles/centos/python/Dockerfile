ARG BASE_IMAGE=centos
ARG BASE_IMAGE_TAG=centos7
FROM ${BASE_IMAGE}:${BASE_IMAGE_TAG}
ARG PYTHON_VERSION=3.8.0
RUN mkdir -p /dataflow/{bin,lib,share,python-envs,r-envs}
#COPY 
RUN yum install -y wget \
    && yum install -y gcc openssl-devel bzip2-devel libffi-devel make \
    && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
    && tar xvf Python-${PYTHON_VERSION}.tgz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure --enable-optimizations \
    && make altinstall \
    && export PATH=/usr/local/bin:$PATH \
    && rm -rf Python-${PYTHON_VERSION}.tgz
   #&& pip3.8 install -r /dataflow/python-envs/py_requirements.txt --no-cache-dir             

#this image took 973 MB
#this needs centos7 as tag