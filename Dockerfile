# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Activate the virtual environment and run app.py using Waitress
CMD ["sh", "-c", "source myenv/bin/activate && waitress-serve --host=0.0.0.0 --port=8080 app:app"]
