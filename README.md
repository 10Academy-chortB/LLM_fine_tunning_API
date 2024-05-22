# LLM Fine-Tuning API
This repository contains scripts for scraping data and performing preprocessing tasks necessary for fine-tuning large language models (LLMs). It is designed to provide a flexible and scalable foundation for future development of an API for fine-tuning LLMs.

## Table of Contents
- [Feature](#features)
- [Project Structure](#projectstructure)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Features
Data Scraping: Scripts to scrape data from various sources defined in a configuration file.
Data Preprocessing: Functions to clean and preprocess scraped data.
Extensible Design: Modular structure to easily add more functionalities in the future.

## Project Structure
- .github
  - workflows
    - workflow.yml
- scripts
  - api
  - automation
  - data_annotation
  - data_collection
      - create_raw_database.py
      - facebook_scrapper.py
      - scrapper.py
      - utils.py
  - data_preprocessing
      - clean_text.py
      - create_preprocessed_database.py
      - database_operations.py
      - preprocess.py
  - create_database.py
  - schema.sql
- .gitignore
- news_sources.json
- requirements.txt

## Installation
To get started with this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/10Academy-chortB/LLM_fine_tunning_API.git
cd LLM_fine_tunning_API
pip install -r requirements.txt
```
Ensure you have the necessary environment setup, including Python 3.8+ and any other dependencies specified in the requirements.txt file.

## Usage
Configure Data Sources: Update the config_json.json file with the information about the websites and sources you want to scrape. Below is an example configuration:

Run Data Scraping: Execute the scrape.py script to scrape data from the configured sources.

```bash
python scripts/data_collection/scrape.py
```
Run Data Preprocessing: Execute the preprocess.py script to preprocess the scraped data.

```bash
python scripts/data_preprocessing/preprocess.py
```

## Contributing
We welcome contributions to this project. To contribute:

## Fork the repository.
Create a new branch for your feature or bugfix.
Make your changes and commit them with descriptive messages.
Push your changes to your fork.
Open a pull request to the main repository.
Please ensure your code adheres to the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

