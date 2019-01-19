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
    orgcount = table.scan(FilterExpression=Attr('type').eq(1))
    channlecount = table.scan(FilterExpression=Attr('type').eq(2))
    cardcount = table.scan(FilterExpression=Attr('type').eq(3))
    stats=[{"type":1,"cnt":orgcount["Count"],"name":"Organizations"},{"type":2,"cnt":channlecount["Count"],"name":"Channels"},{"type":3,"cnt":cardcount["Count"],"name":"cards"}]
    print(type(stats))
    return {
        "statusCode": 200,
         "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        "body": json.dumps(stats,cls=DecimalEncoder)
        
    }