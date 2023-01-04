Amazon AWS EC2
==============

.. code-block:: yaml

    # Crate AWS role:
    #   https://console.aws.amazon.com/iamv2/home#/users
    #
    # Setup:
    #   $ pip install ansible boto3 botocore
    #   $ export AWS_ACCESS_KEY_ID='...'
    #   $ export AWS_SECRET_ACCESS_KEY='...'
    #
    # Run:
    #   $ ansible-playbook ec2.yaml -t ec2_create

    - name: "Launch Amazon AWS EC2 Instances"
      hosts: "localhost"
      connection: "local"
      gather_facts: no

      vars:
        project: "szkolenie_dev"
        vm_region: "eu-central-1"
        vm_image: "ubuntu-jammy-22.04-amd64-server"
        vm_count: 3
        vm_type: "t2.micro"
        hdd_size_root: 20  # size is in GB
        pubkey_path: "~/.ssh/id_rsa.pub"

      tasks:
        - name: "Import public keys from localhost current user to AWS Key Pairs"
          tags: ["ec2_create", "ec2_keypair"]
          amazon.aws.ec2_key:
            region: "{{ vm_region }}"
            name: "{{ project }}"
            key_material: "{{ lookup('file', pubkey_path) }}"

        # https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_security_group_module.html
        - name: "Create AWS Security Group"
          tags: ["ec2_create", "ec2_securitygroup"]
          amazon.aws.ec2_security_group:
            name: "{{ project }}"
            description: "Security Group for {{ project }}"
            region: "{{ vm_region }}"
            rules:
              - proto: "tcp"
                ports: 22
                cidr_ip: "0.0.0.0/0"
              - proto: "tcp"
                ports:
                  - 80
                  - 443
                  - 8080-8099
                cidr_ip: "0.0.0.0/0"
            rules_egress:
              - proto: "all"
                cidr_ip: "0.0.0.0/0"

        - name: "Gather information about Ubuntu LTS AMI"
          tags: ["ec2_create"]
          amazon.aws.ec2_ami_info:
            owner: "099720109477"
            region: "{{ vm_region }}"
            filters:
              name: "ubuntu/images/hvm-ssd/{{ vm_image }}-*"
          register: ami

        # https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_instance_module.html
        - name: "Launch EC2 instances with public IP address"
          tags: ["ec2_create"]
          register: status
          amazon.aws.ec2_instance:
            name: "{{ project }}"
            state: "running"
            exact_count: "{{ vm_count }}"
            region: "{{ vm_region }}"
            key_name: "{{ project }}"
            instance_type: "{{ vm_type }}"
            image_id: "{{ ami.images[-1].image_id }}"
            cpu_credit_specification: "standard"
            security_group: "{{ project }}"
            detailed_monitoring: false
            network:
              assign_public_ip: true
              delete_on_termination: true
            volumes:
              - device_name: "/dev/sda1"  # / - Root folder
                ebs:
                  volume_size: "{{ hdd_size_root }}"
                  volume_type: "gp3"
                  delete_on_termination: true
              # - device_name: "/dev/sda1"
              #   ebs:
              #     volume_size: 0  # size is in GB
              #     volume_type: "gp3"
              #     delete_on_termination: true

        - name: "Get Running instance Info"
          tags: ["ec2_create"]
          ec2_instance_info:
            region: "{{ vm_region }}"
            filters:
              "tag:Name": "{{ project }}"
          register: all

        - name: "Public IPs of all project instances"
          tags: ["ec2_create"]
          debug:
            msg: "{{ all.instances | map(attribute='public_ip_address', default='') }}"

