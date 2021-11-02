# Vehicles web Scraper
* This Project scraps vehicles from [Edmunds Cars](https://www.edmunds.com/cars-for-sale-by-owner/)
* It saves the Vehicles in Excel workbook.

## Made with
* [Python](https://www.python.org/)
* Scrapy - [Docs](https://docs.scrapy.org/en/latest/index.html)
* Openpxyl - [Docs](https://openpyxl.readthedocs.io/en/stable/index.html)

## Table Of Contents
* [Project Setup](#project-setup)
* [Running the Crawler](#running-the-crawler)


## Project Setup
* Unzip the Project into desired location with tool of choice.
* Open terminal in the Uncompressed Folder
    ```bash
    & cd web-scrapper
    ```

* Create Virtual Environment & Activate it.
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
    * for window use:
        ```bash
        $ py -m venv env
        $ .\env\Scripts\activate
        ```

* Install the dependancies
    ```bash
    pip install -r requirements.txt
    ```
    * for windows
    ```bash
    py -m pip install -r requirements.txt
    ```

## Running the Crawler
* To Crawl:
    ```bash
    $ scrapy crawl vehicle_spider
    ```

* Crawl and Out put to json file
    ```bash
    $ scrapy crawl vehicle_spider -O data/vehicles.json
    ```
* Crawl with a radius
    ```bash
    $ scrapy crawl vehicle_spider -a radius=10
    ```