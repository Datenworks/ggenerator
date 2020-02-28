from src.lib.writers.file import FileWriter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter

writers = {
    'file': FileWriter,
    's3': S3RemoteWriter,
    's3-url': S3PresignedUrlRemoteWriter
}
