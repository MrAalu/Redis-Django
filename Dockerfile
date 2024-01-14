FROM python:3.12-alpine

WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies using pip
RUN pip install -r requirements.txt


COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata populateDatabase.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]