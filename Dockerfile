FROM python:3.6

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 7500
CMD ["./entrypoint.sh"]
