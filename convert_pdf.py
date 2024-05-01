import os
import tabula
import glob

# Function to convert tables from PDF to CSV
def convert_pdf_tables_to_csv(pdf_path, csv_folder):
    # Read PDF tables
    dfs = tabula.read_pdf(pdf_path, pages='all')
    
    # Create the CSV folder if it doesn't exist
    os.makedirs(csv_folder, exist_ok=True)
    
    # Convert each DataFrame to CSV
    for i, df in enumerate(dfs):
        df.to_csv(os.path.join(csv_folder, f'{os.path.basename(pdf_path)}_table{i}.csv'))

# Get the directory where the script resides
script_dir = os.path.dirname(__file__)

# Set the default paths for PDF and CSV folders

pdf_folder = os.path.join(script_dir, "PDF")
csv_folder = os.path.join(script_dir, "CSV")

# Check if the PDF folder exists

if not os.path.isdir(pdf_folder):
    print("PDF folder not found. Please create a folder named 'PDFs' and place it in your pdf-scraper folder")
    exit()

# Iterate over PDF files in the folder
for pdf_file in glob.glob(os.path.join(pdf_folder, "*.pdf")):
    convert_pdf_tables_to_csv(pdf_file, csv_folder)

print("Conversion completed successfully.")
