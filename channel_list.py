import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    # TODO implement
    
    table = dynamodb.Table('connectall')
    result = table.query(
    ProjectionExpression="#yr, details.channelname,sk,pk",
    ExpressionAttributeNames={ "#yr": "details.channelname" }, # Expression Attribute Names for Projection Expression only.
    KeyConditionExpression=Key('pk').eq(eval(event["body"])["orgID"]))
    
    return {
        "statusCode": 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        "body": json.dumps(result['Items'],cls=DecimalEncoder)
        
    }