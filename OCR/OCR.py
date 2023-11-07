import boto3
import os 

"""

session = boto3.Session(aws_access_key_id='<your_access_key_id>', aws_secret_access_key='<your_secret_access_key>')

#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('stackvidhya')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)

"""



list_doc =  ['csv_files/',
    ,'csv_files/IRIS.csv'
    ,'df.csv'
    ,'dfdd.csv'
    ,'file2_uploaded_by_boto3.txt'
    ,'file3_uploaded_by_boto3.txt'
    ,'file_uploaded_by_boto3.txt'
    ,'filename_by_client_put_object.txt'
    ,'text_files/'
    ,'text_files/testfile.txt' ]

    
folder_names =[]
doc_name =[]
for doc in list_doc:
    if doc - 4