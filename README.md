# ScrapMagic

1. Below things we goin to impliment in this project 
* Creating your first Scrapy spider
* Crawling through websites & scraping data from each page
* Cleaning data with Items & Item Pipelines
* Saving data to CSV files, MySQL & Postgres databases
* Using fake user-agents & headers to avoid getting blocked
* Using proxies to scale up your web scraping without getting banned
* Deploying your scraper to the cloud & scheduling it to run periodically


2. Setting Up Python Virtual Environment On Linux
* sudo apt-get update
* apt install tree
* sudo apt install -y python3-venv
* python3 -m venv venv
* source venv/bin/activate

3. Create the Scrapy project

* scrapy startproject <project_name>  I have given BooksToScrape  as i am scrapping this.
* scrapy startproject bookscraper

below folder structure will be created
├── scrapy.cfg
└── bookscraper
#Scrapy Project Structure
.
├── BooksToScrape
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       └── __init__.py
└── scrapy.cfg

* Scrapy automatically genrate above template once we create the project using scrapy.
* 5 main building blocks of every Scrapy project: Spiders, Items, Middlewares, Pipelines and Settings.

* settings.py : This file helps us to control entire project

* item.py : is a model for the extracted data. You can define a custom model (like a ProductItem) that will inherit the Scrapy Item class and contain your scraped data.

* pipelines.py is where the item yielded by the spider gets passed, it’s mostly used to clean the text and connect to file outputs or databases (CSV, JSON SQL, etc).

* middlewares.py is useful when you want to modify how the request is made and scrapy handles the response.

* scrapy.cfg is a configuration file to change some deployment settings, etc.


#Creating Our Scrapy Spider

start creating our first Scrapy Spider.

To create a new generic spider, simply run the genspider command:

scrapy genspider bookspider books.toscrape.com


# Cleaning the Scraped data
* As we seen Alredy we have some issue in data and not clean, In this section we doing an data cleaening process. converting to numbers and removing an whitspaces. For this we use pipelines.py




