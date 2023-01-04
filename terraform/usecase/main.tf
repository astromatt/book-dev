###########
## SetUp ##
###########

terraform {
  required_version = "~> 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.15.1"
    }
  }
}


###############
## Variables ##
###############

# This is only variable declaration with
# default values specification
#
# Values will be overriden by `terraform.tfvars`

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "infra"
}

variable "project_stage" {
  description = "Project stage, choices:  dev, test, staging, prod"
  type        = string
  default     = "dev"
}

variable "vm_pubkey" {
  description = "Public Key path to inject to VM"
  type        = string
  default     = "/Users/mwatney/.ssh/id_rsa.pub"
}

variable "vm_region" {
  description = "Amazon AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "vm_count" {
  description = "Number of Virtual Machines to create"
  type        = number
  default     = 3
}

variable "vm_type" {
  description = "Virtual machine instance type"
  type        = string
  default     = "t2.micro"
}

variable "vm_image" {
  description = "Virtual Machine instance image"
  type        = string
  default     = "ubuntu-jammy-22.04-amd64-server"
}

variable "vm_hdd_root" {
  description = "Virtual Machine root volume size [Gigabytes]"
  type        = number
  default     = 20
}

variable "vm_hdd_volume" {
  description = "Virtual Machine additional volume size [Gigabytes]"
  type        = number
  default     = 0
}


############
## Output ##
############

output "vm_ip_public" {
  value       = aws_instance.myapp.*.public_ip
  description = "Public IP address of the main server instance"
}


###################
## Main Instance ##
###################

provider "aws" {
  region = var.vm_region
}

resource "aws_instance" "myapp" {
  ami                         = data.aws_ami.ubuntu_lts.id
  count                       = var.vm_count
  associate_public_ip_address = true
  instance_type               = var.vm_type
  user_data                   = file("init.sh")
  key_name                    = aws_key_pair.local_user.key_name

  # root disk
  root_block_device {
    volume_size           = var.vm_hdd_root
    volume_type           = "gp3"
    encrypted             = true
    delete_on_termination = true
  }

  # extra disk
  ebs_block_device {
    device_name           = "/dev/sda1"
    volume_size           = var.vm_hdd_volume
    volume_type           = "gp3"
    encrypted             = true
    delete_on_termination = true
  }

  tags = {
    Name = "${var.project_name}:${var.project_stage}"
  }
}


################
## Public Key ##
################
resource "aws_key_pair" "local_user" {
  public_key = file(var.vm_pubkey)
}


####################
## Security Group ##
####################
resource "aws_security_group" "https" {
  name        = "https"
  description = "Allow incoming traffic to the EC2 Instance"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow incoming HTTP connections"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow incoming HTTPS connections"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outgoing connections"
  }
}


######################
## Operating System ##
######################
data "aws_ami" "ubuntu_lts" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/${var.vm_image}-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
