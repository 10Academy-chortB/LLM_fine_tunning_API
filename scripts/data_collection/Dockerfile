# base image
FROM python:3.9-slim

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy application files
COPY . .

# command to run the web scraping 
CMD ["python", "scraper.py"]

