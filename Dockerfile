FROM python:3.9-slim-buster
RUN pip install flask
WORKDIR /app
COPY app.py .
COPY config.cfg /config/config.cfg
EXPOSE 5000
CMD ["python", "app.py"]
