Following Storage Classes Available
-----------------------------------
1) S3 Standard
2) S3 Standard-Infrequent Access(S3 Standard-IA)
3) S3 One Zone-Infrequent Access
4) S3 Intelligent-Tiering

S3 Standard
-----------
-> Data is stored redundantly across multiple devices in multiple facilities(>=2 AZs). 
   - 99.99% availability.
   - 99.999999999% durability.
-> Designed for frequent access.
   - Perfect for frequently accessed data.
-> Suitable for most workloads.
   - The default storage class.
   - Use cases include websites, content distribution, mobile and gaming applications.

S3 Standard-IA(Designed for infrequent accessed data)
-----------------------------------------------------
-> Rapid Access
   - Used for data that is accessed less frequently but requires rapid access when needed.
-> Less pay to access data.
   - There is a low per gb storage price and a per gb retrival fee.
-> Use cases.
   - Great for long-term storage, backups, and as a data store for disaster recovery files.
   - 99.99% availability & 99.999999999% durability.

S3 One Zone-Infrequent Access
-----------------------------
-> Data is stored redundantly in one availability zone.
-> Costs 20% less than regular S3 standard-IA.
-> Great for long lived infrequently accessed non-critical data.
-> 99.5% availability & 99.999999999% durability.

What happens if we don't know about access data frequently and infrequently? Below is the way.

S3 Intelligent-Tiering
----------------------
-> Automatically moves our data to the most cost-effective tier based on how frequently we access each object.
-> 99.9% availability & 99.999999999% durability.
-> It optimizes cost. Monthly fee of $0.0025 per 1000 objects.

3 Glacier Options
-----------------
1) Glacier Instant Retrival.
2) Glacier Flexible Retrival.
3) Glacier Deep Archive.

Why Glacier?
------------
-> We pay each time we access data.
-> Use only for archiving data.
-> Glacier is cheap storage.
-> Optimized for data that is very infrequently accessed.
-> 99.99% availability availability and 99.999999999% durability.

Glacier Instant Retrival
------------------------
Provides long-term data archiving with instant retrieval time for our data.

Glacier Flexible Retrival
-------------------------
Ideal storage class for archive data that does not require immediate access but needs the flexibility to retrieve large sets of data at no cost such as backups or disaster recovery use cases. Can be minutes or up to 12 hours.

Glacier Deep Archive
--------------------
Cheapest storage class and designed for customers that retain data sets for 7-10 years or longer to meet customer needs and regularly compliance requirements. The standard retrival time is 12 hours and the bulk retrieval time is 48 hours.


