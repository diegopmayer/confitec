from aws_cdk.aws_s3 import Bucket
import awswrangler as wr


# Loading data to S3
class DataLoadingS3:
    def __init__(self, bucket_output) -> None:
        self.bucket_output = f"s3//{bucket_output}"


    # creating bucket in S3
    def create_bucket(self):
        bucket = Bucket(
            scope=self,
            id="bucket-confitec",
            bucket_name=self.bucket_output,
            auto_delete_objects=True,
            block_public_access=False,
            public_read_access=True
        )


    # Ingestion data into S3 as CSV file replacing the existing data
    def insert_into_s3(self, data_input):
        wr.s3.to_csv(
            df=data_input,
            path=f"s3//{self.bucket_output}/processed/",
            mode="overwrite"
        )