import boto3
iam = boto3.client('iam')

# OPTIONAL: detach a policy
iam.detach_user_policy(
 UserName = 'John', 
 PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)

iam.delete_user(UserName='John')
