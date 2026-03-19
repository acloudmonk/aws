import boto3

ses = boto3.client("ses")


def lambda_handler(event, context):
    ses.send_email(
        Source="verified-email@example.com",
        Destination={"ToAddresses": ["verified-email@example.com"]},
        Message={
            "Subject": {"Data": "File Uploaded"},
            "Body": {"Text": {"Data": str(event)}},
        },
    )
    return {"status": "email sent"}
