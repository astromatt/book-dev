Use Cases
=========


SetUp
-----
.. code-block:: console

    $ cat > hosts << EOF
    [myserver]
    127.0.0.1
    EOF


Console
-------
* Use the run command modules as a last resort
* ``command`` module is safer than ``shell``
* ``command`` cannot evaluate variables
* ``-f FORKS`` -  specify number of parallel processes to use (default=5)

.. code-block:: console
    :caption: Console module

    $ ansible myserver -a '/usr/bin/whoami'
    $ ansible myserver -a '/usr/bin/whoami' -f 10
    $ ansible myserver -a '/usr/bin/whoami' -f 10 -u root
    $ ansible myserver -a '/usr/bin/whoami' -f 10 -u root --become


Shell
-----
* ``shell`` can evaluate variables

.. code-block:: console
    :caption: shell module

    $ ansible myserver -m shell -a 'echo $HOME'
    $ ansible myserver -m shell -a 'echo $(/usr/bin/whoami) > /tmp/whoami'


Copy
----
.. code-block:: console
    :caption: copy

    $ ansible myserver -m copy -a 'src=/etc/hosts dest=/tmp/hosts'


File
----
.. code-block:: console
    :caption: file module

    $ ansible myserver -m file -a 'dest=/var/www mode=755 owner=myuser group=mygroup state=directory'


Ping
----
.. code-block:: console

    $ ansible myserver -m ping
    localhost | SUCCESS => {
        "changed": false,
        "ping": "pong"
    }


User
----
.. code-block:: console
    :caption: User module

    $ ansible myserver -m user -a 'name=myuser password=<crypted password here>'
    $ ansible myserver -m user -a 'name=myuser state=absent'


Service
-------
.. code-block:: console
    :caption: Service module

    $ ansible myserver -m service -a 'name=httpd state=started'
    $ ansible myserver -m service -a 'name=httpd state=restarted'
    $ ansible myserver -m service -a 'name=httpd state=stopped'


Playbook
--------
.. code-block:: console

    $ sudo apt update
    $ sudo apt install -y ansible
    $ export ANSIBLE_HOST_KEY_CHECKING=false
    $ mkdir /home/ubuntu/ansible
    $ ssh-keygen -f /home/ubuntu/.ssh/id_rsa -P ""
    $ cp /home/ubuntu/.ssh/id_rsa.pub /home/ubuntu/ansible/authorized_keys

.. code-block:: sh

    cat > /home/ubuntu/ansible/Dockerfile << EOF
    FROM alpine
    EXPOSE 22/tcp
    COPY authorized_keys /home/myuser/.ssh/

    RUN apk add --no-cache python3 sudo openssh openrc \\
     && mkdir /run/openrc \\
     && touch /run/openrc/softlevel \\
     && ssh-keygen -A \\
     && adduser -D myuser \\
     && echo 'myuser:mypassword' |chpasswd \\
     && echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

    CMD /usr/sbin/sshd -D
    EOF

.. code-block:: console

    $ cd /home/ubuntu/ansible/
    $ docker build . -t myhost
    $ docker run -dit --rm -p 2201:22 --name=one myhost
    $ docker run -dit --rm -p 2202:22 --name=two myhost
    $ docker run -dit --rm -p 2203:22 --name=three myhost

.. code-block:: sh

    cat > /home/ubuntu/ansible/hosts << EOF
    myservers:
      hosts:

        one:
          ansible_host: 127.0.0.1
          ansible_port: 2201
          ansible_user: myuser
          ansible_python_interpreter: /usr/bin/python3

        two:
          ansible_host: 127.0.0.1
          ansible_port: 2202
          ansible_user: myuser
          ansible_python_interpreter: /usr/bin/python3

        three:
          ansible_host: 127.0.0.1
          ansible_port: 2203
          ansible_user: myuser
          ansible_python_interpreter: /usr/bin/python3
    EOF

.. code-block:: console

    $ ansible -i hosts all -m ping
    $ ansible -i hosts all -m shell -a hostname
    $ ansible -i hosts all -m shell -a whoami
    $ ansible -i hosts all -m shell -a whoami -b

.. code-block:: sh

    cat > /home/ubuntu/ansible/nginx.conf << EOF
    server {
      listen {{ http_port }};
      root /var/www;
      error_log  /var/log/nginx/error.log debug;

      location / {
      }
    }
    EOF

.. code-block:: sh

    cat > /home/ubuntu/ansible/nginx.yaml << EOF
    - name: Install and configure nginx
      hosts: all
      become: yes

      vars:
        http_port: 80

      tasks:
        - name: Install
          package: name=nginx state=latest
        - name: Configuration
          template: src=nginx.conf dest=/etc/nginx/http.d/default.conf
        - name: Setup
          file: path=/var/www state=directory owner=myuser group=www-data mode=755
        - name: Enable
          service: name=nginx enabled=yes
        - name: Start
          command: nginx -c /etc/nginx/nginx.conf
    EOF

.. code-block:: console

    $ ansible-playbook -i hosts /home/ubuntu/ansible/nginx.yaml
    PLAY [Install and configure nginx] **********************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************
    ok: [two]
    ok: [one]
    ok: [three]

    TASK [Install] ******************************************************************************************************************
    changed: [one]
    changed: [two]
    changed: [three]

    TASK [Configuration] ************************************************************************************************************
    changed: [three]
    changed: [two]
    changed: [one]

    TASK [Setup] ********************************************************************************************************************
    changed: [two]
    changed: [one]
    changed: [three]

    TASK [Enable] *******************************************************************************************************************
    changed: [one]
    changed: [three]
    changed: [two]

    TASK [Start] ********************************************************************************************************************
    changed: [three]
    changed: [two]
    changed: [one]

    PLAY RECAP **********************************************************************************************************************
    one                        : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    three                      : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    two                        : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

.. code-block:: console

    $ ansible -i hosts all -m shell -a 'ps aux'
    three | CHANGED | rc=0 >>
    PID   USER     TIME  COMMAND
        1 root      0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        7 root      0:00 sshd: myuser [priv]
        9 myuser    0:00 sshd: myuser@pts/1
      139 root      0:00 nginx: master process nginx -c /etc/nginx/nginx.conf
      140 nginx     0:00 nginx: worker process
      141 nginx     0:00 nginx: worker process
      155 myuser    0:00 /bin/sh -c /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.8089316-39769-271226869559802/AnsiballZ_command.py && sleep 0
      156 myuser    0:00 /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.8089316-39769-271226869559802/AnsiballZ_command.py
      157 myuser    0:00 ps aux
    one | CHANGED | rc=0 >>
    PID   USER     TIME  COMMAND
        1 root      0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        7 root      0:00 sshd: myuser [priv]
        9 myuser    0:00 sshd: myuser@pts/1
      139 root      0:00 nginx: master process nginx -c /etc/nginx/nginx.conf
      140 nginx     0:00 nginx: worker process
      141 nginx     0:00 nginx: worker process
      155 myuser    0:00 /bin/sh -c /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.790772-39766-31721004708682/AnsiballZ_command.py && sleep 0
      156 myuser    0:00 /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.790772-39766-31721004708682/AnsiballZ_command.py
      157 myuser    0:00 ps aux
    two | CHANGED | rc=0 >>
    PID   USER     TIME  COMMAND
        1 root      0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        7 root      0:00 sshd: myuser [priv]
        9 myuser    0:00 sshd: myuser@pts/1
      139 root      0:00 nginx: master process nginx -c /etc/nginx/nginx.conf
      140 nginx     0:00 nginx: worker process
      141 nginx     0:00 nginx: worker process
      155 myuser    0:00 /bin/sh -c /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.8128817-39768-279274886841803/AnsiballZ_command.py && sleep 0
      156 myuser    0:00 /usr/bin/python3 /home/myuser/.ansible/tmp/ansible-tmp-1658621623.8128817-39768-279274886841803/AnsiballZ_command.py
      157 myuser    0:00 ps aux
