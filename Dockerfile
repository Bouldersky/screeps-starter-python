FROM python:3.5.9

WORKDIR /root
RUN pip3 install virtualenv 
ADD requirements.txt build.py file_expander.py ./
