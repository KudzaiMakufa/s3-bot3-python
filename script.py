import boto3
import os

s3 = boto3.resource('s3', aws_access_key_id="aws_access_key_id", aws_secret_access_key="aws_secret_access_key" , region_name="nyc3"  ,endpoint_url="https://your_aws_endpoint_url" )



def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    bucket = s3.Bucket(bucket_name)
    s3_folder = s3_folder.strip('/retail')
    if local_dir is None:
        local_dir = s3_folder



    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)

download_s3_folder('your_bucket_name', 'bsse_path', 'you_local_base_path')
