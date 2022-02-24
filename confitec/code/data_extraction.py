import pandas as pd


class DataExtraction:
    def __init__(self, local_path) -> None:
        self.file_path = local_path


    # extraction data from local parquet file
    def data_extraction(self):
        data = pd.read_parquet(self.file_path)
        
        return data