FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose Django port
EXPOSE 8000

# Start the Django development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# This line of command for web serv deploy
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "student_management.wsgi:application"]