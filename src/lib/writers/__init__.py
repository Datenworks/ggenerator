from src.lib.writers.file import FileWriter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.lib.writers.remotes.gcs import GCSRemoteWriter
from src.lib.writers.remotes.azure_bs import AzureBlobStorage
from src.lib.writers.\
    remotes.gcs_presigned_url import GCSPresignedUrlRemoteWriter

writers = {
    S3PresignedUrlRemoteWriter.key: S3PresignedUrlRemoteWriter,
    S3RemoteWriter.key: S3RemoteWriter,
    GCSRemoteWriter.key: GCSRemoteWriter,
    AzureBlobStorage.key: AzureBlobStorage
}

uri_writers = {
    FileWriter.key: FileWriter,
    GCSPresignedUrlRemoteWriter.key: GCSPresignedUrlRemoteWriter
}

writers.update(uri_writers)
