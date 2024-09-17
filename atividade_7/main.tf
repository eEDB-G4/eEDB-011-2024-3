provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  token      = var.aws_session_token
}

# criando buckets s3
resource "aws_s3_bucket" "input_bucket" {
  bucket = "eedb-011-input-data-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "eedb-011-enriched-data-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

# Criando fila SQS
resource "aws_sqs_queue" "data_queue" {
  name = "data-processing-queue"
}

# Função Lambda
resource "aws_lambda_function" "s3_to_sqs" {
  function_name = "s3-to-sqs-function"
  role          = "arn:aws:iam::431758890866:role/LabRole"  # Referência ao ARN da Role
  handler       = "lambda-s3-to-sqs.lambda_handler"
  runtime       = "python3.9"
  
  filename      = "lambda/lambda-s3-to-sqs.zip"
  
  environment {
    variables = {
      SQS_QUEUE_URL = aws_sqs_queue.data_queue.url
    }
  }
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.s3_to_sqs.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.input_bucket.arn
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.input_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.s3_to_sqs.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}

# Função Lambda
resource "aws_lambda_function" "sqs_to_rds" {
  function_name = "sqs-to-rds-function"
  role          = "arn:aws:iam::431758890866:role/LabRole"  # Referência ao ARN da Role
  handler       = "lambda-sqs-to-rds.lambda_handler"
  runtime       = "python3.9"
  
  filename      = "lambda/lambda-sqs-to-rds.zip"
  
  environment {
    variables = {
      SQS_QUEUE_URL = aws_sqs_queue.data_queue.url
    }
  }
}


# Adiciona a fila SQS como um trigger para a função Lambda
resource "aws_lambda_event_source_mapping" "sqs_to_lambda" {
  event_source_arn = aws_sqs_queue.data_queue.arn
  function_name    = aws_lambda_function.sqs_to_rds.arn
  enabled          = true
  batch_size       = 10  # Número máximo de registros que a Lambda lê de uma vez
}

# # Notificação de Bucket S3 para Lambda
# resource "aws_s3_bucket_notification" "s3_bucket_notification" {
#   bucket = aws_s3_bucket.input_bucket.id
# 
#   lambda_function {
#     lambda_function_arn = aws_lambda_function.s3_to_sqs.arn
#     events              = ["s3:ObjectCreated:*"]
#   }
# }
# 
# 
# # criar rds
# resource "aws_db_instance" "rds_instance" {
#   allocated_storage    = 20
#   storage_type         = "gp2"
#   engine               = "mysql"
#   engine_version       = "8.0.30"  # Atualize para uma versão suportada
#   instance_class       = "db.t3.micro"  # Atualize para uma classe suportada
#   db_name              = "mydb"
#   username             = "admin"
#   password             = "password123"
#   parameter_group_name = "default.mysql8.0"
#   skip_final_snapshot  = true
# }
# 
#1resource "aws_db_instance" "postgresql_rds" {
#1  identifier              = "my-postgresql-db"
#1  engine                  = "postgres"
#1  engine_version          = "13.3"
#1  instance_class          = "db.t3.micro"
#1  allocated_storage       = 20  # Tamanho em GB
#1  storage_type            = "gp2"
#1  db_name                 = "mydatabase"      # Nome do banco de dados
#1  username                = "admin"           # Nome de usuário
#1  password                = "mysecretpassword" # Senha do banco de dados
#1  parameter_group_name    = "default.postgres13"
#1  skip_final_snapshot     = true
#1  publicly_accessible     = true               # Tornar o RDS acessível publicamente
#1  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
#1  db_subnet_group_name    = aws_db_subnet_group.default.name
#1
#1  # Configuração de backup
#1  backup_retention_period = 7 # Dias de retenção de backup
#1  backup_window           = "03:00-04:00"
#1}

# Defina a VPC específica
data "aws_vpc" "custom_vpc" {
  id = "vpc-09350544576915457"
}

# Buscar as subnets associadas à VPC específica
data "aws_subnets" "custom_subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.custom_vpc.id]
  }
}

# Criar um Security Group para o RDS na VPC específica
resource "aws_security_group" "rds_sg" {
  name        = "rds_security_group"
  description = "Allow PostgreSQL traffic"
  vpc_id      = data.aws_vpc.custom_vpc.id

  ingress {
    from_port   = 5432      # Porta padrão do PostgreSQL
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Acesso público para teste. Em produção, restrinja a um IP específico.
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Criar um grupo de subnets para o RDS na VPC específica
resource "aws_db_subnet_group" "default" {
  name       = "rds-subnet-group"
  subnet_ids = data.aws_subnets.custom_subnets.ids

  tags = {
    Name = "RDS subnet group"
  }
}

# Criar a instância RDS PostgreSQL
resource "aws_db_instance" "postgresql_rds" {
  identifier              = "my-postgresql-db"
  engine                  = "postgres"
  engine_version          = "16.3"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20  # Tamanho em GB
  storage_type            = "gp2"
  db_name                 = "mydatabase"      # Nome do banco de dados
  username                = "postgres"           # Nome de usuário
  password                = "mysecretpassword" # Senha do banco de dados
  # parameter_group_name    = "default.postgres13"
  skip_final_snapshot     = true
  publicly_accessible     = true               # Tornar o RDS acessível publicamente
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.default.name

  # Configuração de backup
  backup_retention_period = 7 # Dias de retenção de backup
  backup_window           = "03:00-04:00"
}

# Outputs para exibir informações do RDS
output "db_endpoint" {
  value = aws_db_instance.postgresql_rds.endpoint
}

output "db_name" {
  value = aws_db_instance.postgresql_rds.db_name
}

output "db_username" {
  value = aws_db_instance.postgresql_rds.username
}

output "db_password" {
  value = aws_db_instance.postgresql_rds.password
  sensitive = true
}
