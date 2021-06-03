#####################################################################
#
# This Dockerfile has all the packages needed to programmatically
# interact with CIMC 3.0 using Python.  This Dockerfile installs the
# following CentOS packages needed to interact with 3.0:
#
#   1. Python 3.6.8 (Python >= 2.7.9 is needed for CIMC 3.0)
#   2. pip3 with Python 3.6.8
#   3. OpenSSL 1.0.1
#   4. Cisco's Python imcsdk library
#   5. DMTF's Python RedFish library (python-redfish-library)
#   6. epel-release and latest Ansible (if the user want to automate
#      anything with CIMC 3.0)
#   7. Python requests library needed to interact with RedFish URIs
#      /redfish/v1/*
#
# Author: Vikram Hosakote (vhosakot@cisco.com)
#
#####################################################################

FROM centos:latest
MAINTAINER vhosakot@cisco.com

RUN yum -y update && yum -y upgrade && yum clean all
RUN yum -y install which wget gcc zlib-devel openssl-devel
RUN yum -y groupinstall "Development tools"

# Install Python 3.6.8
RUN wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz && \
    tar xzf Python-3.6.8.tgz && \
    cd Python-3.6.8 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall && \
    ln -s /usr/local/bin/python3.6 /usr/bin/python3.6.8 && \
    cd .. && \
    rm -rf Python-3.6.8.tgz && \
    rm -rf Python-3.6.8 && \
    python3.6.8 -V

# Install pip3 with Python 3.6.8
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.6.8 get-pip.py && \
    rm -rf get-pip.py && \
    pip3 --version

# Install OpenSSL 1.0.1
RUN yum -y install openssl && \
    openssl version

# Install imcsdk
RUN pip3 install imcsdk

# Install RedFish Python SDK
RUN git clone https://github.com/DMTF/python-redfish-library.git && \
    cd python-redfish-library && \
    python3.6.8 setup.py sdist --formats=zip && \
    cd dist && \
    z=`ls *.zip` && \
    pip3 install $z && \
    cd ../.. && \
    rm -rf python-redfish-library

# Install epel-release latest Ansible
RUN yum -y install epel-release && \
    yum -y install ansible && \
    ansible --version

# Install Python requests library
RUN pip3 install requests

CMD ["sleep", "infinity"]
