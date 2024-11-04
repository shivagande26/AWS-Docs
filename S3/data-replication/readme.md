S3 Replication
--------------
- We can replicate the objects from one bucket to another.
  - Versioning must be enabled in both source and destination buckets.
- Objects in existing bucket were not replicated automatically.
  - Once replication is turned on subsequent updated objects will be replicated automatically.
- Delete markers were not replicated by default.
  - Deleting individual versions or delete markers will not be replicated.

Note : To replicate the existing objects we need to create batch jobs.

Important Points
----------------
- We can replicate the objects from one bucket to another bucket.
- Objects in the existing bucket are not replicated automatically.
- Delete markers were not replicated by default.