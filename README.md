# Python Automation Suite

A collection of 25 standalone Python scripts for everyday automation and utility tasks — file handling, data conversion, web scraping, system utilities and small productivity tools.

## What it does

Each script does one job and runs on its own. Pick a script, install whatever library it needs, and run it with Python. The scripts cover practical scripting: converting files, scraping web pages, sending bulk email, organising folders, watching the system, and more.

## Scripts

| Script | What it does |
|---|---|
| `CLI Todo App.py` | Command-line to-do list app (built with Click) |
| `Calculate Your Age.py` | Age, leap-year and month-days helper functions |
| `Capture Screenshots At Regular Intervals of Time.py` | Takes screenshots on a timer (pyautogui) |
| `Convert JSON to CSV.py` | Converts a JSON file to CSV |
| `Create a simple stopwatch.py` | Stopwatch with a Tkinter GUI |
| `Currency Converter.py` | Currency converter script |
| `Decimal to Binary converter.py` | Converts decimal numbers to binary |
| `Encrypt and Decrypt Texts.py` | AES text encryption and decryption (pycryptodome) |
| `Fetch all links from a given webpage.py` | Extracts every link from a web page (requests + BeautifulSoup) |
| `Find IMDB Ratings.py` | Looks up IMDB ratings and genres for films in a folder and saves them to CSV |
| `Get the IP Address and Hostname of A Website.py` | Resolves a website to its IP address and hostname |
| `Image Watermarking.py` | Adds a watermark to an image (Pillow) |
| `Low Battery Notification.py` | Leap-year and month-days helper functions |
| `Organized download folder with different categories.py` | Sorts a downloads folder into categories |
| `Password Generator.py` | Generates random passwords |
| `Python script to compress folders and files.py` | Compresses folders and files into a zip archive |
| `Scrap and Download all images from the WEB Page.py` | Downloads all images from a web page (Selenium + BeautifulSoup) |
| `Send Emails in Bulk From CSV File.py` | Sends bulk emails from a CSV list (smtplib) |
| `Snapshot of The Given Website.py` | Takes a screenshot of a website (Selenium + ChromeDriver) |
| `Split Files Into Chunks.py` | Splits files into smaller chunks (pandas) |
| `String search from multiple files.py` | Searches for a string across multiple files |
| `Terminal Progress Bar.py` | Terminal progress bar demo (tqdm) |
| `Text To Speech.py` | Converts text to speech (gTTS) |
| `Web Scrapping Youtube Comment.py` | Scrapes YouTube comments (Selenium) |
| `Wifi Password Ejector.py` | Retrieves saved Wi-Fi passwords on the machine (Windows) |

## Tech stack

- Python 3 (standard library for most scripts)
- Third-party libraries used across the suite: `requests`, `beautifulsoup4`, `pandas`, `Pillow`, `selenium`, `pyautogui`, `click`, `pycryptodome`, `tqdm`, `gtts`, `chromedriver-binary`, `tkinter`

## How to run

There is no `requirements.txt` in this repo — install only the libraries the script you want to run needs. To install the commonly used ones in one go:

```bash
pip install requests beautifulsoup4 pandas Pillow selenium pyautogui click pycryptodome tqdm gtts
```

Then run any script directly, for example:

```bash
python "Password Generator.py"
python "Convert JSON to CSV.py"
```

Each script is standalone — no setup or server needed. Some scripts ask for input when they run (for example a file path or a website URL).

## Project structure

```
Python-Automation-Suite/
├── README.md                  # This file
├── CLI Todo App.py
├── Calculate Your Age.py
├── Capture Screenshots At Regular Intervals of Time.py
├── Convert JSON to CSV.py
├── Create a simple stopwatch.py
├── Currency Converter.py
├── Decimal to Binary converter.py
├── Encrypt and Decrypt Texts.py
├── Fetch all links from a given webpage.py
├── Find IMDB Ratings.py
├── Get the IP Address and Hostname of A Website.py
├── Image Watermarking.py
├── Low Battery Notification.py
├── Organized download folder with different categories.py
├── Password Generator.py
├── Python script to compress folders and files.py
├── Scrap and Download all images from the WEB Page.py
├── Send Emails in Bulk From CSV File.py
├── Snapshot of The Given Website.py
├── Split Files Into Chunks.py
├── String search from multiple files.py
├── Terminal Progress Bar.py
├── Text To Speech.py
├── Web Scrapping Youtube Comment.py
└── Wifi Password Ejector.py
```
