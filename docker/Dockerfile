# 
FROM python:3.11.3

# 
WORKDIR /code

# 
COPY ../backend/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
CMD ["bash", "-c", "wait-for-it --service postgres:5432 --timeout 300 && ls &&cd app && python run.py"]
