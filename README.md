
# Confitec Project Solution


## Objective
> Create an ETL Solution for getting parquet format data from local stage and processing this data based on stakehouders requirements with Python/PySpark and load into S3 bucket.


## Requirements from stakehouder
[Documentation](/docs/Avaliação_Confitec.pdf)


## Technology
* Python
* Pyspark
* AWS CDK, CLI, AWSWrangler, EMR, S3


## Credentials
* You must create the named profiles with AWS CLI
* First, create the named profile configure -> [AWS Profile Configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods)
* Loading environment variables from named profile -> [Environment variable](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)


## Using
Install all dependencies and activating virtual environment
Linux
```
$ bash source.sh
```
Windows
```
$ source.bat
```
