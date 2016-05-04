# module_oceana

Instructions for running module:
{
install boto and storages via
pip install boto
pip install django-storages
}
You will need id and secret key for uploading on s3 bucket.
In oceana/setting.py ,replace the below code with valid id and secret key

{
AWS_S3_ACCESS_KEY_ID = '...'     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = '...' # enter your secret access key
}
