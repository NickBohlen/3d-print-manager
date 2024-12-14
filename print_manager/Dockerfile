# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files (if you're using Django static files)
RUN python manage.py collectstatic --noinput

RUN apt-get update && apt-get install -y \
    python3-opencv \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the application (replace with your desired start command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]