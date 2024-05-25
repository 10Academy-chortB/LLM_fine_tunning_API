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
CMD ["python", "create_raw_database.py", "facebook_scraper.py", "lyrics.py", "scraper.py", "utils.py"]

