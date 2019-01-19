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
    ProjectionExpression="#yr, details.organizationame,sk",
    ExpressionAttributeNames={ "#yr": "details.organizationame" }, # Expression Attribute Names for Projection Expression only.
    KeyConditionExpression=Key('pk').eq("123e4567-e89b-12d3-a456-426655440000"))
    print(type(result['Items']))
    return {
        "statusCode": 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        "body": json.dumps(result['Items'],cls=DecimalEncoder)
    }