import os
import requests
import zipfile

def download_and_unzip(file_url, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Specify the path where the zip file will be saved
    zip_path = os.path.join(output_folder, 'file.zip')

    # Download the file from the given URL
    print(f"Downloading from {file_url}...")
    response = requests.get(file_url)
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    print("Download complete!")

    # Unzip the downloaded file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    # Remove the zip file after extraction
    os.remove(zip_path)

    print(f"Downloaded and extracted files to: {output_folder}")
