import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('connectall')
   
    timestamp = int(time.time() * 1000)
    cardId=str(uuid.uuid1())
    item = {
        
        'pk':eval(event["body"])["chnId"],
        'sk':cardId+str(timestamp),
        'details':eval(event["body"]),
        'type':3,
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
