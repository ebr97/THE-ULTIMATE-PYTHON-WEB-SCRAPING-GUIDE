<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a>
# Automate Google Sheets with gspread API

In this project I will use gspread API to automatically update Google Sheets whenever the web scraper is run. This functionality is similar with creating a Database, because the user will have all the data in one place without creating aditional files.

## Use cases
The main purpose of this project is to deliver a scraper that can be used by anyone who need to scrape data from web on regullary basis without altering the old data that may have.

## How it works
The scraper will look after the URL column in Google Sheet and retrive all the links in a list. Is built in such a manner that it will look after the Date column too and will run only for the links that are added in the current day. In this way the scraper won't send unnecessary request to servers for the oldest links.

In order for scraper to run you'll need firstly to go to Google APIs and create a new project. There you'll need to add the Google Sheets API and Google Drive API. Then you'll need to go to keys and create new KEY, the right format for that key is JSON and download it. Then you'll need to share the Google Sheet project and in the email address you will put the 'client-email' that is in the KEY that you've downloaded. The final step will be to add the gspread API into your Python script and that's it

## Files
main.py is the web scraper and cred.json represent the KEY that you've downloaded. These two files need to be in the same folder in order to work properly

## Demonstration Video


https://user-images.githubusercontent.com/90221077/166903238-d908d417-67c2-4db4-83d6-be49648bd4f7.mp4



