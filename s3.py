import json
import boto3

s3 = boto3.client('s3',aws_access_key_id='AKIASFPZKHWG5RCUZ775',
                    aws_secret_access_key='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')


bucket = "aws-product-data"
key = "products.json"
response = s3.get_object(Bucket = bucket,Key = key)
content = response['Body']
jsonObject = json.loads(content.read())
products = jsonObject['products']
for record in products:
    print("productName: "+ record["productName"])
    print("cost: "+ record["cost"])
    print("-------")

