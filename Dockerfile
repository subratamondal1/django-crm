FROM python:3.11-slim
WORKDIR /app

# Copy "requirements.txt" file from this FOLDER (DJANGO-CRM) to the CONTAINER APP
COPY requirements.txt .

# Update the package list and install the required system dependencies
RUN apt-get update && \
    apt-get install -y pkg-config default-libmysqlclient-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Install the Python dependencies from "requirements.txt"
RUN pip install --no-cache-dir -r requirements.txt

# Copy each and everything from this ROOT FOLDER (DJANGO-CRM) to the CONTAINER ROOT APP
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
