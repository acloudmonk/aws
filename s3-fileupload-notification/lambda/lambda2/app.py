import boto3

ses = boto3.client("ses")


def lambda_handler(event, context):
    ses.send_email(
        Source="sachinsingh2005@gmail.com",
        Destination={"ToAddresses": ["sachinsingh2005@gmail.com"]},
        Message={
            "Subject": {"Data": "File Uploaded"},
            "Body": {"Text": {"Data": str(event)}},
        },
    )
    return {"status": "email sent"}
