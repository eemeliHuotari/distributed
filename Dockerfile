# Start with the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the port the gRPC server will run on
EXPOSE 50051

# Run the gRPC server
CMD ["python", "grpc_server.py"]
