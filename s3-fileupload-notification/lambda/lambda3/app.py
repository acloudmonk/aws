import boto3
import os

sns = boto3.client("sns")
TOPIC_ARN = os.environ["TOPIC_ARN"]


def lambda_handler(event, context):
    message = f"File uploaded: {event['key']} in bucket {event['bucket']}"

    sns.publish(TopicArn=TOPIC_ARN, Message=message)

    return {"status": "email via sns sent"}
