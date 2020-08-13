 AKIAVE6J6RJPI2B5YTY5
 dimi3fTm4t8vhQ6myF51mqpyqzdWb1T559oZknff

 import boto3
iam = boto3.client('iam')

# create a user
iam.create_user( UserName='John')

# attach a policy
iam.attach_user_policy(
 UserName = 'John',
 PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)
