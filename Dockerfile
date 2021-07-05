FROM python:3
ADD file_uploader.py /
ADD RTC.zip /
RUN pip install flask
RUN pip install flask_restful
RUN pip3 install minio
CMD [ "python", "./file_uploader.py"]