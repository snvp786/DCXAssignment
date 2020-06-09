import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    paramkey = 'UserName'
    bucketname = 'dxcassignment'
    s3 = boto3.resource('s3')
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name=paramkey, WithDecryption=True)
    s3object = s3.Object(bucketname, 'paramnew.json')
    paramvalue = parameter['Parameter']['Value']
    jsondata = {"name":paramkey, "value":paramvalue}
    s3object.put(Body=(bytes(json.dumps(jsondata).encode('UTF-8')))
    
)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
