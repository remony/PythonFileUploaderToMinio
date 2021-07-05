from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "minio.minio:9000",
        access_key="admin",
        secret_key="P@ssw0rd",
        secure=False
    )

    # Make 'rtc' bucket if not exist.
    found = client.bucket_exists("rtc")
    if not found:
        client.make_bucket("rtc")
    else:
        print("Bucket 'rtc' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "rtc", "RTC.zip", "/RTC.zip",
    )
    print(
        "'/RTC.zip' is successfully uploaded as "
        "object 'RTC.zip' to bucket 'rtc'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)