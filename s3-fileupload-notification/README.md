# 🚀 AWS Serverless Notification System

## 📌 Overview
This project demonstrates a serverless event-driven architecture using AWS SAM.

## Versions Used:
SAM CLI, version 1.155.2
pip-26.0.1
Python 3.12.0

## 🔄 Workflow
1. File uploaded to S3
2. EventBridge triggers Step Function
3. Lambda1 reads SSM parameter
4. Decision:
   - SES → Email
   - SNS → Notification

## 🛠 Tech Stack
- AWS SAM
- Lambda (Python)
- Step Functions
- EventBridge
- S3
- SSM Parameter Store
- SES / SNS

## 💡 Features
- Dynamic notification routing
- Fully serverless
- Cost-optimized (Free Tier friendly)

## 🚀 Deployment

```bash
sam build
sam deploy --guided