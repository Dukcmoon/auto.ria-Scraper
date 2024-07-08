# auto.ria-Scraper

## Overview
auto.ria-Scraper is a web scraping project designed to gather car listings from various websites and store them in a SQLite database. The project includes functionality to filter and upload car data to a JSON file based on user-specified criteria.

## Features
- Scrapes car listings and stores them in a SQLite database.
- Filters car listings based on model, mileage, and price.
- Uploads filtered car listings to a JSON file.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Dukcmoon/auto.ria-Scraper
   cd auto.ria-Scraper
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Scraper:**
   To start the web scraper and gather car listings, use the following command:
   ```sh
   python main.py scrapy
   ```

2. **Filter and Upload Car Listings:**
   To filter car listings based on model, mileage, and price, and then upload the filtered data to a JSON file, use the following command:
   ```sh
   python main.py upload --model <car_model> --mileage <max_mileage> --price <max_price>
   ```

   You will be prompted to enter the car model, mileage, and price if not specified in the command. Use `0` for any criteria you wish to ignore.

## Project Structure

- `CarSpider/`: Directory containing the Scrapy project.
- `upload_filtered_cars_to_json.py`: Script to filter and upload car listings to a JSON file.
- `requirements.txt`: File listing all the required Python packages.
- `README.md`: Project documentation.

## Example Commands

1. **Run the Scraper:**
   ```sh
   python main.py scrapy
   ```

2. **Filter and Upload Car Listings:**
   ```sh
   python main.py upload --model "Toyota" --mileage 50000 --price 20000
   ```

   Or run without options to be prompted:
   ```sh
   python main.py upload
   ```

## Dependencies

The project requires the following Python packages, specified in `requirements.txt`:

- attrs==23.2.0
- Automat==22.10.0
- certifi==2024.2.2
- cffi==1.16.0
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- constantly==23.10.4
- cryptography==42.0.2
- cssselect==1.2.0
- filelock==3.13.1
- hyperlink==21.0.0
- idna==3.6
- incremental==22.10.0
- itemadapter==0.8.0
- itemloaders==1.1.0
- jmespath==1.0.1
- lxml==5.1.0
- packaging==23.2
- parsel==1.8.1
- Protego==0.3.0
- pyasn1==0.5.1
- pyasn1-modules==0.3.0
- pycparser==2.21
- PyDispatcher==2.0.7
- PyMySQL==1.1.0
- pyOpenSSL==24.0.0
- queuelib==1.6.2
- requests==2.31.0
- requests-file==2.0.0
- Scrapy==2.11.0
- service-identity==24.1.0
- six==1.16.0
- tldextract==5.1.1
- Twisted==22.10.0
- urllib3==2.2.0
- w3lib==2.1.2
- zope.interface==6.1

## Author

by goosvel and ZaslavkyDi 

---
