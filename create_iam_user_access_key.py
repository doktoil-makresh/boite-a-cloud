import boto3

client = boto3.client('iam')
response = client.create_access_key(
    UserName='string'
)
