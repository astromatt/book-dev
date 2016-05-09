# Environment Access

## Environment Setup

    apt-get install --yes git vim nmap htop wget curl unzip

## Locale

    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales

## TODO

Enable password login in /etc/ssh/sshd_config (easy for windows users with putty)

    ssh -i workshop.pem -l ubuntu HOST_IP_ADDRESS
    apt-get install --yes git vim nmap htop wget curl unzip
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales
    sudo passwd ubuntu

