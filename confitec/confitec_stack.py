from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda


class ConfitecStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        fn = _lambda.Function(
            scope=self,
            id="LambdaConfitecETL",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset(path.join(__dirname, "confitec/code"),
                bundling=BundlingOptions(
                    image=_lambda.Runtime.PYTHON_3_9.bundling_image,
                    command=["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
                    ]
                )
            ),
            timeout=cdk.Duration.minutes(amount=5)
        )

