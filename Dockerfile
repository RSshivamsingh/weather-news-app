
# 1. Use an official Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your app code
COPY . .

# 5. Tell Docker to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
