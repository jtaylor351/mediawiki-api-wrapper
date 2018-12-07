FROM ubuntu:xenial

# installing graph tool
RUN echo "deb http://downloads.skewed.de/apt/xenial xenial universe\n" >> /etc/apt/sources.list
RUN echo "deb-src http://downloads.skewed.de/apt/xenial xenial universe\n" >> /etc/apt/sources.list
RUN apt-get -y update && apt-get -y upgrade
RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
RUN apt-get -y --allow-unauthenticated install python3-graph-tool
RUN apt-get install -y openmpi-bin libopenmpi-dev graphviz cifs-utils libffi-dev pkg-config libcairo2-dev 
RUN apt-get -y update && apt-get -y upgrade

# set up environment
RUN mkdir /output
RUN mkdir /working
COPY . /working

# installing pip
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip 
RUN pip3 install -r /working/requirements.txt --ignore-installed
