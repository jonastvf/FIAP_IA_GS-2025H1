FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]