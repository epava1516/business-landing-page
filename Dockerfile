FROM python:3.11.3-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Copy project dependencies
COPY requirements.txt /code/

# Install project dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Run django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]