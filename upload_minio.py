from minio import Minio
import os

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('192.168.14.42:9000',
                    access_key='AKIAIOSFODNN7EXAMPLE',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    secure=False)

# Function to upload a directory to a Minio bucket.
def upload_directory(directory, bucket_name, minioClient):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'rb') as file_data:
                file_stat = os.stat(file_path)
                minioClient.put_object(bucket_name, file_path, file_data, file_stat.st_size)


# Upload directory 'test' to Minio bucket 'my-bucketname'
upload_directory('site', 'asiatrip', minioClient)
