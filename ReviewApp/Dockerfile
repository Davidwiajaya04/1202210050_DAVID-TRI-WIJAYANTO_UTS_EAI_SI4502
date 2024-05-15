# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container's workspace.
COPY . .

# Make the container's port 5003 available to the outside
EXPOSE 5003

CMD ["python", "review_app.py"]
