import json

def lambda_handler(event, context):
    # TODO implement
    consumers={
	"load": "Load Type : House",
    "Location": "Location : Gobabis,Namibia"
  }
 
    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(consumers)
    }
