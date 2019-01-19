import json
import boto3
import logging
import uuid

sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    # TODO implement
    name = str(uuid.uuid1())
    c=creatingqueue(name)
    s=sendingmessage(name)
    
    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(c)
    }

def creatingqueue(name):
     queue = sqs.create_queue(QueueName=name, Attributes={'DelaySeconds': '5'})
     return name
     

def sendingmessage(name):
     queue = sqs.get_queue_by_name(QueueName=name)
     for i in range(1,7):
        response =queue.send_message(MessageBody=str(i), MessageAttributes={
    'Author': {
        'StringValue': 'Deepak',
        'DataType': 'String'
    }
})
     return response