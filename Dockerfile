FROM python:3.10
WORKDIR /app
COPY app /app/
RUN pip install --upgrade -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]

