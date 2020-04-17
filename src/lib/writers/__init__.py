from src.lib.writers.file import FileWriter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.lib.writers.remotes.gcs import GCSRemoteWriter
from src.lib.writers.remotes.azure_bs import AzureBSRemoteWriter
from src.lib.writers.\
    remotes.gcs_presigned_url import GCSPresignedUrlRemoteWriter
from src.lib.writers.databases.mysql import MysqlClientDatabaseWriter, \
    MysqlDirectDatabaseWriter
from src.lib.writers.databases.postgresql import PostgresDirectDatabaseWriter,\
    PostgreSqlClientDatabaseWriter

writers = {
    S3PresignedUrlRemoteWriter.key: S3PresignedUrlRemoteWriter,
    S3RemoteWriter.key: S3RemoteWriter,
    GCSRemoteWriter.key: GCSRemoteWriter,
    AzureBSRemoteWriter.key: AzureBSRemoteWriter
}

uri_writers = {
    FileWriter.key: FileWriter,
    GCSPresignedUrlRemoteWriter.key: GCSPresignedUrlRemoteWriter
}

database_writers = {
    'mysql-cli': MysqlClientDatabaseWriter,
    'mysql-direct': MysqlDirectDatabaseWriter,
    'postgres-cli': PostgreSqlClientDatabaseWriter,
    'postgres-direct': PostgresDirectDatabaseWriter
}

writers.update(uri_writers)
writers.update(database_writers)
