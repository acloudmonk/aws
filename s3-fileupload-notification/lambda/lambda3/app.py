import boto3

sns = boto3.client("sns")


def lambda_handler(event, context):
    sns.publish(PhoneNumber="+91XXXXXXXXXX", Message=f"File uploaded: {event}")
    return {"status": "sms sent"}
