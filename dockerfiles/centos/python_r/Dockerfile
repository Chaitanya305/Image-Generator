ARG BASE_IMAGE=centos
FROM ${BASE_IMAGE}:centos7
ARG R_VERSION=4.3.2
ARG OS_IDENTIFIER=centos-7
ARG PYTHON_VERSION=3.8.0
RUN mkdir -p /dataflow/{bin,lib,share,python-envs,r-envs}
#COPY
# Install R
RUN yum install wget -y && \
    wget https://cdn.posit.co/r/${OS_IDENTIFIER}/pkgs/R-${R_VERSION}-1-1.x86_64.rpm && \
    yum -y install epel-release && \
    yum -y install ./R-${R_VERSION}-1-1.x86_64.rpm && \
    ln -s /opt/R/${R_VERSION}/bin/R /usr/bin/R && \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/bin/Rscript && \
    ln -s /opt/R/${R_VERSION}/lib/R /usr/lib/R && \
    rm R-${R_VERSION}-1-1.x86_64.rpm && \
    yum -y remove epel-release && \
    #install pyhton
    yum install -y gcc openssl-devel bzip2-devel libffi-devel make && \
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar xvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make altinstall && \
    export PATH=/usr/local/bin:$PATH && \
    rm -rf ../Python-${PYTHON_VERSION}.tgz && \
    #pip3.8 install -r /dataflow/python-envs/py_requirements.txt --no-cache-dir && \
    yum clean all

    #this image size is 1.44