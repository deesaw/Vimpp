## Creating and Using Amazon S3 Buckets
"""
--------------------------------------------------------------------------------
This Python example shows you how to:

- Obtain and display a list of Amazon S3 buckets in your account.
- Create an Amazon S3 bucket.
- Upload an object to a specified bucket.

In this example, Python code is used to obtain a list of existing
Amazon S3 buckets, create a bucket, and upload a file to a specified bucket.
The code uses the AWS SDK for Python to get information from and upload
files to an Amazon S3 bucket using these methods of the Amazon S3 client class:

. list_buckets
. create_bucket
. upload_file
--------------------------------------------------------------------------------
"""




## Display a List of Amazon S3 Buckets
"""
********************************************************************************
List all the buckets owned by the authenticated sender of the request.

The example below shows how to:

- List buckets using list_buckets.
********************************************************************************
"""
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)




## Create an Amazon S3 Bucket
"""
********************************************************************************
The example below shows how to:

- Create a new bucket using create_bucket.
********************************************************************************
"""
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucket')




## Upload a File to an Amazon S3 Bucket
"""
********************************************************************************
The example below shows how to:

- Upload a file to a bucket using upload_file.
********************************************************************************
"""
import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'file.txt'
bucket_name = 'my-bucket'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)
