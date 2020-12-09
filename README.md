# VIRTUAL EXHIBIT

### “Agham at Teknolohiya: Sandigan ng Kalusugan, Kabuhayan, Kaayusan at Kinabukasan”

BY DEPARTMENT OF SCIENCE AND TECHNOLOGY | REGION 3

---

### Superuser Credentials:

#### ADMIN Account

- Username: dostr3admin
- Email: dostr3admin@gov.ph
- Password: WxLSTvSS45KVpmw9Bbn9

#### STAFF Account

- Username: dostr3staff
- Email: dostr3staff@gov.ph
- Password: eKU74yKfHv8qCCYqbJad

#### Gmail Account

- Email: dostregionthree@gmail.com
- Password: 5@yTPmv&-R_TrT4b

#### PUBLIC IPv4

- http://54.179.75.226/

#### AWS DBMS

- Username:
- Password:
- Endpoint:
- Port: 3306
- DBName:

#### NOTES:

1. Remove `dostr3djangoserver.pem` file in deployment-stage

#### AWS CORS Configuration

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "HEAD"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]
```

#### AWS Bucket Policy

```
{
    "Version": "2012-10-17",
    "Id": "Policy1606146582729",
    "Statement": [
        {
            "Sid": "Stmt1606146580838",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::dost-ve-bucket/*"
        }
    ]
}
```
