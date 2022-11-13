import pulumi
from pulumi_aws import s3

# Create an S3 bucket on AWS
bucket = s3.Bucket('my-bucket-pulumi-cloud-demo',
                   acl='public-read',
                   tags={
                       'Environment': 'Dev',
                       'Name': 'MyPulumiBucket',
                       'Owner': 'Devenes',
                       'Project': 'PulumiCloud',
                       'Team': 'DevOps'
                   },
                   versioning={
                       'enabled': True
                   },
                   website=s3.BucketWebsiteArgs
                   (
                       index_document="index.html",
                       error_document="error.html"
                   )
                   )

bucketObject = s3.BucketObject(
    'index.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html')
)

bucketObject = s3.BucketObject(
    'error.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket.id,
    source=pulumi.FileAsset('error.html')
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

pulumi.export('bucket_endpoint', pulumi.Output.concat
              (
                  'http://', bucket.website_endpoint
              ))
