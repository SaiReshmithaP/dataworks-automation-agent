# Step 1: Use the official Python 3.10+ image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the application code into the container
COPY . .

# Step 5: Expose the port FastAPI will run on
EXPOSE 8000

# Step 6: Set environment variables (ensure AIPROXY_TOKEN is passed securely)
ENV AIPROXY_TOKEN=""

# Step 7: Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
