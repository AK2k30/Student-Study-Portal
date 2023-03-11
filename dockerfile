FROM python:3.11

WORKDIR /app
# COPY studentstudyportal/ /app/
COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
