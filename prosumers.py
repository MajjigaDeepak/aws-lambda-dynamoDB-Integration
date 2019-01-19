import json

def lambda_handler(event, context):
    # TODO implement
    prosumers= [{
    "title": "Prosumer 1",
    "description":"We are generating solar Energy from roof top solar pannels with 15KW capacity.",
    "producer": "Location : Windhoek,Namibia",
    "price": "Price in KWH : 10",
    "rating": "Quality : 100%"
  },
  {
    "title": "Prosumer 2",
    "description":"We are generating solar Energy from roof top solar pannels with 10KW capacity.",
    "producer": "Location : Walvis Bay,Namibia",
    "price": "Price in KWH : 20",
    "rating": "Quality : 95%"
  },
  {
    "title": "Prosumer 3",
    "description":"We are generating solar Energy from roof top solar pannels with 35KW capacity.",
    "producer": "Location : Swakopmund,Namibia",
    "price": "Price in KWH : 30",
    "rating": "Quality : 90%"
    
  }
]
 
    return {
        'statusCode': 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(prosumers)
    }
