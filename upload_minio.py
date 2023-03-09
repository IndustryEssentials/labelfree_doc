from minio import Minio
import os
import glob
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
            # with open(file_path, 'rb') as file_data:
            #     file_stat = os.stat(file_path)
            # minioClient.put_object(
            #             bucket_name, file_path, file_data, file_stat.st_size)
            res = minioClient.fput_object(bucket_name, f"site/{file_path}", file_path)
            print(res.geturl())
              


# delete directory 'test' from Minio bucket 'my-bucketname'
def deleteFolder(bucketname, folderName):
    # Delete using "remove_object"
    objects_to_delete = minioClient.list_objects(
        bucketname, prefix=folderName, recursive=True)
    for obj in objects_to_delete:
        minioClient.remove_object(bucketname, obj.object_name)

deleteFolder('labelfree', 'site')

# Upload directory 'test' to Minio bucket 'my-bucketname'
upload_directory('site', 'labelfree', minioClient)
