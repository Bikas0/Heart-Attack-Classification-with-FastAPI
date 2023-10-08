FROM python:3.9
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
EXPOSE 8080
CMD ["uvicorn", "MLTrainingProject:app", "--host", "0.0.0.0", "--port", "8080"]