from data_extraction import DataExtraction
from data_process import DataProcess
from data_load import DataLoadingS3


def handler(event, context):


    # call the data extraction
    data = DataExtraction(
        local_path='data/OriginaisNetflix.parquet'
    )

    # Create the Bucket
    data_load = DataLoadingS3(
        bucket_output="confitec-data-processed"
    )
    #creating bucket and ingestion data to bucket
    data_load.create_bucket()

    # call the data process
    process = DataProcess(data)
    data_processed = process.data_process()

    # loading data into s3
    data_load.insert_into_s3(data_input=data_processed)
