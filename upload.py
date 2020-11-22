import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'airy-berm-296308-c65c251b6472.json'
cwd = os.path.abspath(os.getcwd())

client = storage.Client()
bucket = client.get_bucket('taxi_csv')

def upload_to_gcs(filename):
    blob = bucket.blob(filename)
    blob.upload_from_filename(os.path.join(cwd, 'CSVs\\', filename))
    print(f'{filename} uploaded to gsc')

def move_file(filename):
    path = os.path.join(cwd, 'CSVs\\', filename)
    new_path = os.path.join(cwd, 'CSVs\\Processed\\', filename)
    os.rename(path,new_path)


csv_files = [file for file in os.listdir(cwd + '\\CSVs') if file.endswith('.csv')]

for csv in csv_files :
    upload_to_gcs(csv)
    move_file(csv)