from minio import Minio
import os

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('192.168.12.137:9000',
                    access_key='labelfree',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    secure=False)

# Function to upload a directory to a Minio bucket.
def upload_directory(directory, bucket_name, minioClient):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            object_name = os.path.join(bucket_name, file_path)
            res = minioClient.fput_object(bucket_name, object_name, file_path)


# Upload directory 'test' to Minio bucket 'my-bucketname'
upload_directory('site', 'asiatrip', minioClient)
