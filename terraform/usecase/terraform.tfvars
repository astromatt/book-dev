# Project
project_name  = "infra"
project_stage = "dev" # dev, test, staging, prod

# Virtual Machine
vm_region     = "eu-central-1"
vm_image      = "ubuntu-jammy-22.04-amd64-server"
vm_type       = "t2.micro"
vm_pubkey     = "/Users/mwatney/.ssh/id_rsa.pub"
vm_count      = 1
vm_hdd_root   = 20 # GB
vm_hdd_volume = 0  # GB
