# Best to match host OS. Run on host:
# lsb_release -r
FROM ubuntu

RUN apt-get update
RUN apt-get -y upgrade
### ADD YOUR TOOLS HERE
RUN apt-get -y install software-properties-common
RUN apt -y install python3 python3-pip git nano cmake g++ wget unzip
RUN pip install numpy matplotlib tensorflow
