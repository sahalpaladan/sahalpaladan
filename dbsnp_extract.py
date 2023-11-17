#This code written for extract the genomic and chromosomal positions for rsids from dbsnp database
#Create excel file Column heading rsID and add rsids in that column
#Replace the input excel file as your file
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace 'rsids' with a list of the rsids you want to scrape
rsids = pd.read_excel("/home/sahal/commants/PGx/Genotype_from_vcf/rs2.xlsx")
rsids = rsids["rsID"]

# Create an empty DataFrame to store all the data
dfs = []

for rsid in rsids:
    # Construct the URL for each rsid
    url = f'https://www.ncbi.nlm.nih.gov/snp/{rsid}#variant_details'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table on the webpage
        table = soup.find('table', {'id': 'genomics_placements_table'})

        if table:
            # Extract data from the table
            table_data = []
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all(['th', 'td'])
                row_data = [column.text.strip() for column in columns]
                table_data.append(row_data)

            # Convert the data to a pandas DataFrame
            df = pd.DataFrame(table_data[1:], columns=table_data[0])

            # Add a column with the rsid for reference
            df['RSID'] = rsid

            # Append the data to the main DataFrame
            dfs.append(df)

        else:
            print(f"Table not found for rsid {rsid}")
    else:
        print(f"Failed to retrieve the webpage for rsid {rsid}. Status code: {response.status_code}")
all_data = pd.concat(dfs, ignore_index=True)
# Save the combined DataFrame to an Excel file
all_data.to_excel('combined_data.xlsx', index=False)
print("Data saved to 'combined_data.xlsx'")
