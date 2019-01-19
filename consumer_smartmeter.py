import json
import boto3
import logging


sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    # TODO implement
    queue = sqs.get_queue_by_name(QueueName=eval(event["body"])["qname"]);
    
    
    if len(queue.receive_messages())>0:
        message=queue.receive_messages()[0]
        x=message.body
        message.delete()
    else:
        queue.delete(QueueUrl=queue.url)
        x=0
    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(x)
    }

