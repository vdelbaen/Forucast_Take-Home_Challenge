gcloud config set project airy-berm-296308

gsutil mb -p airy-berm-296308 -c Standard -l europe-west1 -b on gs://taxi_csv

gcloud functions deploy bq_insert --region=europe-west1 --runtime=python38 --trigger-event=google.storage.object.finalize --trigger-resource=taxi_csv --source=.\cloud_function --service-account=fourcast-take-home-challenge-s@airy-berm-296308.iam.gserviceaccount.com --entry-point=bq_insert