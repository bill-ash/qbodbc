FROM python:3.9.6-alpine3.14

COPY ./script.py . 
COPY ./requirements.txt . 

RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/bill-ash/qbodbc

CMD ["python3", "script.py"]