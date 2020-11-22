from google.cloud import bigquery

client = bigquery.Client()

table_id = "airy-berm-296308.Fourcast_Take_Home_Challenge.taxi_location_data_batch"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("unique_key", "STRING"),
        bigquery.SchemaField("taxi_id", "STRING"),
        bigquery.SchemaField("trip_start_timestamp", "TIMESTAMP"),
        bigquery.SchemaField("trip_end_timestamp", "TIMESTAMP"),
        bigquery.SchemaField("pickup_latitude", "FLOAT"),
        bigquery.SchemaField("pickup_longitude", "FLOAT"),
        bigquery.SchemaField("dropoff_latitude", "FLOAT"),
        bigquery.SchemaField("dropoff_longitude", "FLOAT"),
        bigquery.SchemaField("pickup_latlong", "STRING"),
        bigquery.SchemaField("dropoff_latlong", "STRING"),
        bigquery.SchemaField("pickup_community_area", "INTEGER"),
        bigquery.SchemaField("dropoff_community_area", "INTEGER"),

    ],
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    source_format=bigquery.SourceFormat.CSV,
)


def bq_insert(data, context):
    print('new csv file {} uploaded, inserting to BigQuery...'.format(data['name']))
    uri = "gs://" + data['bucket'] + "/" + data['name']
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))