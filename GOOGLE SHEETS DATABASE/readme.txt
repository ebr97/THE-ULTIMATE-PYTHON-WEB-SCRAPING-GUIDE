# Google Sheets Database with Python Web Scraping

In this project, I'll use gspread API to create something similar to a database in Google Sheets. This API allows our Python script to communicate with Google Sheets and allows automatic sheet updates when the script is run. In this case, we will have the URL column with links that need to be scrapped. When the scraper is run the sheets will automatically update with all the necessary data.

#### Key aspects about this file

In this case, we only want to scrape the links from the current day without altering the ones from previous days. For that we need the Date column, which values need to be manually inserted whenever there are new links inserted, after all the links for that day are inserted we can run our Python script.
