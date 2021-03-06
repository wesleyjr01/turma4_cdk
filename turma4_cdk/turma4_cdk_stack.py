from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class Turma4CdkStack(cdk.Stack):
    bucket_name = 'bucket-belisco-cdk-turma444'
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        s3.Bucket(self, id=self.bucket_name, bucket_name=self.bucket_name)
        # The code that defines your stack goes here
