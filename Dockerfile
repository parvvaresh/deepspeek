FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the model download script
RUN chmod +x dl_model.sh && ./dl_model.sh

# Expose the application port (modify if needed)
EXPOSE 9090

# Set environment variables (modify as needed)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["python", "app.py"]
