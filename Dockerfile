# Use an official Rasa image as a base
FROM rasa/rasa:3.6.20-full

# Set the working directory
WORKDIR /app

# Copy your Rasa project files into the container
COPY . /app

# Optionally, install any additional dependencies if needed
# RUN pip install ...

# Expose the port your Rasa server will run on
EXPOSE 5005

ENTRYPOINT ["rasa"]

# Command to start Rasa server
CMD ["run", "-m", "models", "--enable-api", "--cors", "*"]