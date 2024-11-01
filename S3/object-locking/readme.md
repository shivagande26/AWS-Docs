S3 Object Lock
--------------
We can use s3 object lock to store objects using a "write once read many(WORM)" model. It can help prevent objects from being deleted or modified for a fixed amount of time or indefinately.
We can use s3 object lock to meet regulatory requirements that require worm storage, or add an extra layer of protection against object changes or deletion.

We have two different modes
1) Governance Mode
2) Compliance Mode

Governance Mode
---------------
In governance mode, Users can't delete an object version or alter its lock settings unless they have special permissions.
With governance mode, We protect objects against being deleted by most users, But still we can grant some user permissions to alter the retention settings or delete the object if necessary.

Compliance Mode
---------------
In compliance mode, A protected object version cannot be overridden or deleted by any user including root user. If the object is locked in compliance mode its retention period cannot be shortened.
Compliance mode ensures an object version can't be overwritten or deleted for the duration of the retention period.

Retention Period
----------------
A retention period protects an object version for a fixed amount of time. When we place a retention period on an object version, Amazon s3 stores a timestamp in the object version's metadata to indicate when the retention period expires.
After the retention period expires, The object version can be overwritten or deleted unless we also place a legal hold on the object version.

Legal Hold
----------
S3 object lock also enable us to place an legal hold on an s3 object version. Like a retention period legal hold also prevents an object from being overwritten or deleted.
However a legal hold doesn't have an associated retention period and remains in effect until removed. 
Legal holds can be freely placed or removed by any user who has the s3:PutObjectLegalHold permission.

Glacier Vault Lock
------------------
S3 glacier vault lock allows us to easily deploy and enforce compliance controls for individual s3 glacier vaults with the vault lock policy. We can specify controls such as WORM in a vault lock policy and lock the policy from future edits. Once locked the policy can no longer be changed.

Important Points
----------------
Use s3 object lock to store objets using a write once read many(WORM) model.
Object lock can be on individual objects or applied across the bucket as a whole.
Object lock comes in two modes Governance Mode and Compliance Mode.
S3 glacier vault lock allows us to easily deploy and enforce compliance controls for individual s3 glacier vaults with vault lock policy.
We can  specify controls such as WORM in a vault lock policy and lock the policy for future edits. Once locked the policy can no longer be changed.