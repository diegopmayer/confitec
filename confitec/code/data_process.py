import awswrangler as wr
import boto3


class DataProcess:
    def __init__(self, data) -> None:
        self.data = data


    def data_process(self):

        data_processed = self.data

        return data_processed