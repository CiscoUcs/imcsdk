#####################################################################
#
# This Dockerfile has all the packages needed to programmatically
# interact with CIMC 3.0 using Python.  This Dockerfile installs the
# following CentOS packages needed to interact with 3.0:
#
#   1. Python 2.7.13 (Python >= 2.7.9 is needed for CIMC 3.0)
#   2. pip with Python 2.7.13
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

# Install Python 2.7.13
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz && \
    tar xzf Python-2.7.13.tgz && \
    cd Python-2.7.13 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall && \
    ln -s /usr/local/bin/python2.7 /usr/bin/python2.7.13 && \
    cd .. && \
    rm -rf Python-2.7.13.tgz && \
    rm -rf Python-2.7.13 && \
    python2.7.13 -V

# Install pip with Python 2.7.13
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python2.7.13 get-pip.py && \
    rm -rf get-pip.py && \
    pip --version

# Install OpenSSL 1.0.1
RUN yum -y install openssl && \
    openssl version

# Install imcsdk
RUN pip install imcsdk

# Install RedFish Python SDK
RUN git clone https://github.com/DMTF/python-redfish-library.git && \
    cd python-redfish-library && \
    python2.7.13 setup.py sdist --formats=zip && \
    cd dist && \
    z=`ls *.zip` && \
    pip install $z && \
    cd ../.. && \
    rm -rf python-redfish-library

# Install epel-release latest Ansible
RUN yum -y install epel-release && \
    yum -y install ansible && \
    ansible --version

# Install Python requests library
RUN pip install requests

CMD ["sleep", "infinity"]
