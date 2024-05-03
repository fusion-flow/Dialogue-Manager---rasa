# Use an official Rasa image as a base image
FROM rasa/rasa:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the trained model into the container
COPY ./models/core.tar.gz /app/models/

# Expose the port on which your Rasa Core server will run
EXPOSE 5005

# Command to run when the container starts
CMD ["run", "-m", "models", "--enable-api", "--cors", "*"]
