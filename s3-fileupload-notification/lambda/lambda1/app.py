import boto3

ssm = boto3.client("ssm")


def lambda_handler(event, context):
    param = ssm.get_parameter(Name="/notification_type")
    notification_type = param["Parameter"]["Value"]

    return {
        "notification_type": notification_type,
        "bucket": event.get("bucket"),
        "key": event.get("key"),
    }
