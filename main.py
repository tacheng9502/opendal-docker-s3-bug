from opendal import Operator
import os

# Load S3 configuration from environment variables
s3_bucket = os.getenv("S3_BUCKET")
s3_region = os.getenv("S3_REGION")
s3_access_key = os.getenv("S3_ACCESS_KEY")
s3_secret_key = os.getenv("S3_SECRET_KEY")
s3_object_path = os.getenv("S3_OBJECT_PATH")

# Initialize OpenDAL operator for S3
operator = Operator(
    "s3",
    **{
        "bucket": s3_bucket,
        "region": s3_region,
        "access_key_id": s3_access_key,
        "secret_access_key": s3_secret_key,
    },
)

# Attempt to stat the object
try:
    result = operator.stat(s3_object_path)
    print("Stat Result:", result)
except Exception as e:
    print("Error:", e)
