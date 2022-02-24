FROM python:3.8
RUN cd root
WORKDIR /root

ADD src /root

CMD ["python3", "/root/main_function.py"]
