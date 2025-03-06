🌐 AWS Blog Web Page Infrastructure 🚀

📖 Project Description

This project aims to build a scalable, secure, and highly available blog web page infrastructure on AWS. The architecture includes EC2 instances hosted in private and public subnets, a load balancer (ALB), NAT Gateway, S3, CloudFront, Route 53, and other AWS services. MySQL is used as the database, and the data is stored in a private subnet within the VPC.

🏗 Architectural Components

1️⃣ VPC (Virtual Private Cloud)

🏢 An isolated network environment with private and public subnets.

2️⃣ Subnets

🔒 Private subnets: Used for the blog web page and MySQL database.

🌍 Public subnets: Used for the NAT instance and load balancer (ALB).

3️⃣ NAT Instance

🔄 Enables internet access for private subnet servers while maintaining security.

4️⃣ Load Balancer (ALB - Application Load Balancer)

⚖️ Distributes traffic among scalable web servers.

5️⃣ Auto Scaling Group

📈 Automatically scales web servers based on traffic demand.

6️⃣ S3 Buckets

🖼 Stores images and videos for the blog web page.

📂 A separate S3 bucket is available for failover scenarios.

7️⃣ CloudFront

🚀 A content delivery network (CDN) that accelerates the delivery of static content.

8️⃣ Route 53

🌎 Manages DNS and domain routing.

9️⃣ VPC Endpoints

🔐 Provides secure connectivity to AWS services.

🔟 DynamoDB

⚡️ A fast and scalable NoSQL database for the blog application.

1️⃣1️⃣ Lambda Functions (With S3 Role)

🤖 Used for automated workflows and serverless computing.

🔧 Requirements

To deploy this project, you need the following:

✅ AWS Account
✅ AWS CLI (To manage AWS services via the command line)
✅ Terraform or AWS CloudFormation (To manage infrastructure as code)
✅ Bash or PowerShell (To execute commands)
✅ MySQL Database (Amazon RDS or manually installed on EC2)

💡 Note: Ensure that you have the necessary IAM roles and permissions configured before deployment!
