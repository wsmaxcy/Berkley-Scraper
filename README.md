# Webpage Email Scraper

This Python program scrapes email addresses from a list of webpages. It uses the `requests` library to make HTTP requests and retrieve the webpage content, and the `BeautifulSoup` library to parse the HTML content. The program uses regular expressions to extract email addresses from the HTML.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)

## Usage

1. Clone the repository or download the script file.

2. Install the required libraries by running the following command:

```bash
pip install requests beautifulsoup4
```

3. Open the script file and replace the `url` variable with the URL of the webpage you want to scrape.

```python
python webPull.py
```

4. Run the script using the following command:

5. The program will scrape the webpage and print the extracted email address(es) to the console.

This example scrapes a JSON API response containing a list of organizations from the provided URL. It then extracts the email addresses from each organization's webpage and prints them to the console.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).


