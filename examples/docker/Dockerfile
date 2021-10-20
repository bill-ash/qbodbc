FROM python:3.9.6-windowsservercore-1809

# The only way to call QuickBooks from Docker is 
# is through a linked server connection. 

COPY ./script.py . 
COPY ./requirements.txt . 

RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/bill-ash/qbodbc

CMD ["python3", "script.py"]