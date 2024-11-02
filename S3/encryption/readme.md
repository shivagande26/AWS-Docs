Types Of Encryption
-------------------
1) Encryption in transit
   - SSL/TLS
   - HTTPS
2) Encryption at rest : Server side encryption
   - SSE-S3 : S3 managed keys using AES 256 bit encryption.
   - SSE-KMS : AWS key management service managed keys.
   - SSE-C : Keys provided by us.
3) Encryption at rest : Client side encryption
   - We encrypt the file before uploading to S3.

All amazon s3 buckets have encryption enabled by default. All objects are automatically encrypted using server side encryption with SSE-S3.
This encryption settings applied to all objects in our s3 buckets.

Enforcing Server Side Encryption By Following Below Ways
--------------------------------------------------------
1) x-amz-server-side-encryption
   If the file is to be encrypted at upload time, the x-amz-server-side-encryption parameter will be included in the request header.
2) Two options
   x-amz-server-side-encryption: AES256 (SSE-S3 -> S3 managed keys)
   x-amz-server-side-encryption: aws:kms (SSE-KMS -> KMS managed keys)
3) PUT request header
   When this parameter is included in header of the PUT request it tells S3 to encrypt the object at the time of upload using the specified encryption method.

We can create a bucket policy that denies any S3 PUT request that doesn't include the x-amz-server-side-encryption parameter in the request header.

Important Points
----------------
Encryption In Transit
- SSL/THS
- HTTPS

Encryption At Rest: SSE
- Server-side encryption
- SSE-S3(AES 256-bit)
- SSE-KMS
- SSE-C

Client Side Encryption
We encrypt the files ourselves before uploading to S3.

Enforcing Encryption With A Bucket Policy
A bucket policy can deny all PUT requests that don't include the x-amz-server-side-encryption parameter in the request header.
