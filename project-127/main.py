import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape star data
def scrape_stars_data():
    # URL of the Wikipedia page with the list of stars
    url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

    # Open the URL and read the HTML content
    with urllib.request.urlopen(url) as response:
        html_content = response.read()

    # Parse the HTML content of the page
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table with class 'wikitable'
    table = soup.find('table', class_='wikitable')

    # List to store scraped data
    stars_data = []

    # Find all rows (tr) in the table body (tbody)
    rows = table.find('tbody').find_all('tr')

    # Iterate over rows
    for row in rows[1:]:  # Skip the header row
        # Find all cells (td) in the row
        cells = row.find_all('td')

        # Extract data from cells if they exist
        if len(cells) >= 6:
            # Get star name, distance, mass, radius, and luminosity
            star_name = cells[0].text.strip()
            distance = cells[5].text.strip()
            mass = cells[7].text.strip()
            radius = cells[8].text.strip()
            luminosity = cells[9].text.strip()

            # Append the data to the list
            stars_data.append([star_name, distance, mass, radius, luminosity])

    return stars_data

# Main function
def main():
    # Scrape star data
    data = scrape_stars_data()

    # Create DataFrame from scraped data
    df = pd.DataFrame(data, columns=['Star Name', 'Distance', 'Mass', 'Radius', 'Luminosity'])

    # Save DataFrame to CSV
    df.to_csv('stars_data.csv', index=False)

if __name__ == "__main__":
    main()
