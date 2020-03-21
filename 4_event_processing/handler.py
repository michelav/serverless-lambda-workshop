import base64

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_sqs(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

    for record in event["Records"]:
        msg = record["body"]
        logger.info(f"Got a SQS event: {msg}")

def handle_sns(event, context):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html

    for record in event["Records"]:
        msg = record["Sns"]["Message"]
        logger.info(f"Got a SNS event: {msg}")
    pass

def handle_kinesis(event, content):
    # See https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

    for record in event["Records"]:
        msg = base64.b64decode(record["kinesis"]["data"])
        logger.info(f"Got a Kinesis event: {msg}")
    pass
