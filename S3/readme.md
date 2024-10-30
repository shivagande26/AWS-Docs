What is S3
----------
-> S3 provides secure, durable and highly scalable object storage.
-> S3 allows you to store and retrieve any amount of data from anywhere on web at a very low cost.
-> Amazon S3 is easy to use with a simple web service interface.
-> Built for 99.95%-99.99% service availability depending on S3 tier.
-> Designed for 99.999999999% durability for data stored in S3.

Characteristics
---------------
-> Tired Storage.
   S3 offers a range of storage classes designed for different use cases.
-> Lifecycle Management.
   Define rules to automatically transition objects to a cheaper storage tier or delete objects that are no longer required after a set period of time.
-> Versioning.
   With versioning all versions of objects are stored and can be retrieved.

Securing Our Data
------------------
-> Serverside Encryption.
   We can set default encryption on a bucket to encrypt all new objects when they are stored in the buckets.
-> Access Control Lists(ACLs).
   Define which AWS accounts or groups are granted access and the type of access. We can attach S3 ACLs to individual objects as well.
-> Bucket Policies.
   S3 bucket policies specifies what actions are allowed or denied.

Important Points To Remember
----------------------------
-> S3 is an object based storage allows us to upload files.
-> Not suitable to install any OS or run any database.
-> Files can be uploaded to S3 with the size from from 0 bytes to 5TB.
-> The number of objects we can upload to S3 is unlimited.