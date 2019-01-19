import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('connectall')
   
    timestamp = int(time.time() * 1000)
    channelId=str(uuid.uuid1())
    item = {
        
        'pk':eval(event["body"])["pkid"],
        'sk':eval(event["body"])["pkid"]+channelId,
        'details':eval(event["body"]),
        'type':2,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    table.put_item(Item=item)

    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(eval(event["body"])["pkid"]+channelId)
    }
