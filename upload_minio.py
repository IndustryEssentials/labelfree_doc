from minio import Minio
import os

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('192.168.12.137:9000',
                    access_key='labelfree',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    secure=False)

# Function to upload a directory to a Minio bucket.


def upload_local_directory_to_minio(local_path: str, bucket_name: str):
    assert os.path.isdir(local_path)

    for local_file in glob.glob(local_path + '/**'):
        local_file = local_file.replace(os.sep, "/")
        if not os.path.isfile(local_file):
            upload_local_directory_to_minio(
                local_file, bucket_name)
        else:
            remote_path = os.path.join(
                local_file[1 + len(local_path):])
            remote_path = remote_path.replace(
                os.sep, "/")
            minioClient.fput_object(bucket_name, remote_path, local_file)


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
