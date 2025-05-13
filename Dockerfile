FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's port
EXPOSE 7860

# Run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]