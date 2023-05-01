
provider "aws" {
  region = "us-west-1"
}

resource "aws_sns_topic" "ec2_provisioning_topic" {
  name = "ec2-provisioning-topic"
}

##################### LAMBDA DEPLOYMENT PACKAGE #####################
data "archive_file" "ec2_provisioning_lambda" {
  type = "zip"

  source_dir  = "./archive/src"
  output_path = "./archive/ec2_provisioning_lambda.zip"
}

resource "aws_lambda_function" "ec2_provisioning_lambda" {
  filename         = "./archive/ec2_provisioning_lambda.zip"
  function_name    = "ec2_provisioning_lambda"
  role             = aws_iam_role.ec2_provisioning_lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = data.archive_file.ec2_provisioning_lambda.output_base64sha256
  runtime          = "python3.9"
  timeout          = 30

  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.ec2_provisioning_topic.arn
    }
  }
}

resource "aws_iam_role" "ec2_provisioning_lambda_role" {
  name = "ec2_provisioning_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "ec2_provisioning_lambda_policy" {
  name = "ec2_provisioning_lambda_policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
      {
        Action = [
          "sns:Publish"
        ]
        Effect   = "Allow"
        Resource = aws_sns_topic.ec2_provisioning_topic.arn
      }
    ]
  })

  depends_on = [
    aws_iam_role.ec2_provisioning_lambda_role
  ]
}

resource "aws_iam_role_policy_attachment" "ec2_provisioning_lambda_policy_attachment" {
  policy_arn = aws_iam_policy.ec2_provisioning_lambda_policy.arn
  role       = aws_iam_role.ec2_provisioning_lambda_role.name
}

resource "aws_cloudwatch_event_rule" "ec2_provisioning_event_rule" {
  name        = "ec2-provisioning-event-rule"
  description = "Monitors EC2 provisioning events"

  event_pattern = jsonencode({
    source      = ["aws.ec2"]
    detail_type = ["AWS API Call via CloudTrail"]
    detail = {
      eventSource = ["ec2.amazonaws.com"]
      eventName   = ["RunInstances"]
      userIdentity = {
        type     = ["IAMUser"]
        userName = ["YOUR_USERNAME"]
      }
    }
  })
}

resource "aws_cloudwatch_event_target" "ec2_provisioning_event_target" {
  rule = aws_cloudwatch_event_rule.ec2_provisioning_event_rule.name
  arn  = aws_lambda_function.ec2_provisioning_lambda.arn
}

# To test the code, you can use the following Python code
# import boto3

# client = boto3.client('ec2')

# # Provision an EC2 instance
# instance = client.run_instances

# =========================
