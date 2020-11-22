SELECT DISTINCT
    unique_key
  , taxi_id
  , trip_start_timestamp
  , trip_end_timestamp
  , pickup_latitude
  , pickup_longitude
  , dropoff_latitude
  , dropoff_longitude
  , CONCAT(pickup_latitude,"," ,pickup_longitude)  AS pickup_latlong
  , CONCAT(dropoff_latitude,"," ,dropoff_longitude)  AS dropoff_latlong
  , pickup_community_area
  , dropoff_community_area
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE pickup_location IS NOT NULL
  AND dropoff_location IS NOT NULL
  AND pickup_location <> dropoff_location
  AND trip_start_timestamp >= '2019-01-01 00:00:00 UTC'
  
 UNION ALL
 
 SELECT DISTINCT *
 FROM `airy-berm-296308.Fourcast_Take_Home_Challenge.taxi_location_data_batch`