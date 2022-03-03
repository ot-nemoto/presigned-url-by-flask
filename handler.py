# -*- coding: utf-8 -*-

import os
import boto3

from flask import Flask

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', '')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', '')
region_name = os.getenv('REGION_NAME', 'ap-northeast-1')

bucket = os.getenv('BUCKET', '')
key = os.getenv('KEY', '')
expires_in = os.getenv('EXPIRES_IN', '1800')

s3 = boto3.client(
    service_name='s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

app = Flask(__name__)

@app.route('/presigned-url')
def presigned_url():
    return s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=expires_in,
        HttpMethod='GET'
    )

if __name__ == "__main__":
    app.run(debug=True)
