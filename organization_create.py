import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('connectall')
   
    timestamp = int(time.time() * 1000)
    organizationId=str(uuid.uuid1())
    
    item = {
        
        'pk':"123e4567-e89b-12d3-a456-426655440000",
        'sk':organizationId,
        'details':eval(event["body"]),
        'type':1,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    table.put_item(Item=item)

    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(organizationId)
    }
