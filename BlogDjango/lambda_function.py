import json
import boto3

def lambda_handler(event, context):
    # S3 ve DynamoDB'yi başlat
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb')
    
    # DynamoDB tablosunun adı
    table_name = 'final-aws'
    table = dynamodb.Table(table_name)
    
    # Olay verilerinden bucket ve dosya adı bilgilerini al
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        
        # İlgili bilgileri DynamoDB'ye kaydet
        response = table.put_item(
            Item={
                'FileName': file_name,
                'BucketName': bucket_name,
                'Timestamp': record['eventTime']
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
