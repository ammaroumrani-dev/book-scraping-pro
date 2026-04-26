# book-scraping-pro
# Python Web Scraper: Bookstore Data Extraction
A Python script developed to extract and organize data from online bookstores. The project focuses on providing clean, structured data ready for analysis.
## Project Details
This tool extracts key product information including:
* Book Titles
* Numerical Prices (Separated from currency symbols)
* Product Ratings
* Stock Availability
## Technical Specifications
* **Libraries:** BeautifulSoup4, Requests, and Pandas.
* **Data Cleaning:** Implemented logic to handle text encoding (UTF-8) and string formatting.
* **Output Formats:** Data is exported to CSV and XLSX (Excel) files.
* **Performance:** Includes request throttling to ensure stable data retrieval.
## File Structure
* main.py: The core Python script.
* books.csv: Raw data output.
* books.xlsx: Formatted Excel report.
## Usage
To run this project, ensure you have Python installed and the required libraries:
pip install beautifulsoup4 requests pandas openpyxl
