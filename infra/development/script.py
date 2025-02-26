import boto3
import json

LOCALSTACK_ENDPOINT = "http://localhost:4566"


def get_sqs_client(session: boto3.Session) -> boto3.client:
    return session.client("sqs", endpoint_url=LOCALSTACK_ENDPOINT)


def get_sns_client(session: boto3.Session) -> boto3.client:
    return session.client("sns", endpoint_url=LOCALSTACK_ENDPOINT)


def create_queue(queue_name: str, session: boto3.Session) -> str:
    sqs = get_sqs_client(session)
    response = sqs.create_queue(QueueName=queue_name)
    return response["QueueUrl"]


def create_topic(topic_name: str, session: boto3.Session) -> str:
    sns = get_sns_client(session)
    response = sns.create_topic(Name=topic_name)
    return response["TopicArn"]


def run():
    AWS_PROFILE = "local"

    # SQS Queue Name
    SQS_QUEUE_NAME = "default-queue"
    SNS_TOPIC_NAME = "default-topic"

    # Create SQS Queue
    session = boto3.Session(profile_name=AWS_PROFILE)
    SQS_QUEUE_URL = create_queue(SQS_QUEUE_NAME, session)
    print(f"SQS Queue Created: {SQS_QUEUE_URL}")

    # Create SNS Topic
    SNS_TOPIC_ARN = create_topic(SNS_TOPIC_NAME, session)
    print(f"SNS Topic Created: {SNS_TOPIC_ARN}")

    # Get SQS Queue ARN
    sqs = get_sqs_client(session)
    response = sqs.get_queue_attributes(
        QueueUrl=SQS_QUEUE_URL, AttributeNames=["QueueArn"]
    )
    SQS_QUEUE_ARN = response["Attributes"]["QueueArn"]
    print(f"SQS Queue ARN: {SQS_QUEUE_ARN}")

    # Subscribe SQS to SNS
    sns = get_sns_client(session)
    sns.subscribe(TopicArn=SNS_TOPIC_ARN, Protocol="sqs", Endpoint=SQS_QUEUE_ARN)
    print("Subscribed SQS to SNS")

    # Set SQS Policy to allow SNS to send messages
    sqs_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "SQS:SendMessage",
                "Resource": SQS_QUEUE_ARN,
                "Condition": {"ArnEquals": {"aws:SourceArn": SNS_TOPIC_ARN}},
            }
        ],
    }

    sqs.set_queue_attributes(
        QueueUrl=SQS_QUEUE_URL, Attributes={"Policy": json.dumps(sqs_policy)}
    )
    print("SQS Policy Set to Allow SNS Messages")


run()
