import pandas as pd
import os

def detect_utf8_bom(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        if raw_data.startswith(b'\xef\xbb\xbf'):  # UTF-8 BOM
            return True
    return False

def read_fidelity_csv(file_path):
    if detect_utf8_bom(file_path):
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    else:
        df = pd.read_csv(file_path, encoding='utf-8')
    return df

def daily_import_workflow():
    # Set the directory where the CSV files are located
    csv_directory = 'path/to/daily/csv/files'
    today = pd.Timestamp.now().date()
    file_name = f'Fidelity_Data_{today}.csv'
    file_path = os.path.join(csv_directory, file_name)
    
    if os.path.isfile(file_path):
        data = read_fidelity_csv(file_path)
        # Process data as needed
        print(data)
    else:
        print(f"File {file_path} does not exist.")

if __name__ == "__main__":
    daily_import_workflow()