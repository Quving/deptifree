FROM python:3.6

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:7500", "deptifree.wsgi"]
