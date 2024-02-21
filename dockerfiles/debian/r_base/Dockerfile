ARG BASE_IMAGE=debian
ARG BASE_IMAGE_TAG=bullseye
FROM ${BASE_IMAGE}:${BASE_IMAGE_TAG}
ARG R_VERSION=4.3.2
ARG OS_IDENTIFIER=debian-11
RUN mkdir -p /dataflow/bin /dataflow/lib /dataflow/share /dataflow/python-envs /dataflow/r-envs
#COPY
# Install R
RUN apt-get update -qq && \
    apt-get install wget -y && \
    wget https://cdn.posit.co/r/${OS_IDENTIFIER}/pkgs/r-${R_VERSION}_1_amd64.deb && \
    DEBIAN_FRONTEND=noninteractive apt-get install -f -y ./r-${R_VERSION}_1_amd64.deb && \
    ln -s /opt/R/${R_VERSION}/bin/R /usr/bin/R && \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/bin/Rscript && \
    ln -s /opt/R/${R_VERSION}/lib/R /usr/lib/R && \
    rm r-${R_VERSION}_1_amd64.deb && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean -y  
CMD ["R"]

#this image took 740MB 