S3 Prefixes
-----------
S3 prefix is just the folder inside the bucket.

S3 Performance 
--------------
- S3 has extremely low latency. We can get the first byte out of S3 within 100-200 milliseconds.
- We can also achieve a high number of requests: 3500 PUT/COPY/POST/DELETE and GET/HEAD requests per second per prefix.
- We can get better performance by spreading our reads across different prefixes. For example if we are using 2 prefixes we will achieve 11000 requests per second.
- If we are using 4 prefixes we can achieve 22000 requests per second.

S3 Limitations When Using KMS
-----------------------------
- If we are using SSE-KMS to encrypt our objects in S3 we must keep in ming the KMS limits.
- When we upload a file, We call "GenerateDataKey" in the KMS api.
- When we download a file we will call "Decrypt" in the KMS api.

KMS Comes With Below Built In Limits
------------------------------------
- Uploading/Downloading will count toward the KMS quota.
- Quota is region specific. It's either 5000, 10000 or 30000 requests per second.
- Currently we cannot request quota increase for KMS.

S3 Performance: Uploads
-----------------------
Multipart Uploads
-----------------
- Recommended for files over 100MB.
- Required for files over 5GB.
- Parallelize our uploads(Increases efficiency).

S3 Performance: Downloads
-------------------------
S3 Byte-Range Fetches
---------------------
- Parallelize downloads by specifying byte ranges.
- If there's a failure in the download, It's only for a specific byte range.

Important Points
----------------
- mybucketname/folder1/subfolder1/myfile.jpg > /folder1/subfolder1
- We can also achieve a high number of requests: 3500 PUT/COPY/POST/DELETE and 5500 GET/HEAD requests per second per prefix.
- We can get better performance by spreading our across different prefixes. For example if we are using 2 prefixes we can achieve 11000 requests per second.
- If we are SSE-KMS to encrypt our objects in s3we must keep in mind KMS limits.
   - Uploading/Downloading will count toward the KMS quota.
   - Quota is region specific. However it's either 5500, 10000 or 30000 requests per second.
   - Currently we cannot request a quota increase for KMS.
- Use multipart uploads to increase performance when uploading files to S3. Should be used for any files over 100MB and must be used for any file over 5GB.
- Use S3 byte range fetches to increase performance when downloading files from s3.s