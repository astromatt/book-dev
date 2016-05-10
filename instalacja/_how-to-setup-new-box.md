# How to setup a new box

Warning: If you are using Linux and provided pendrive cannot be mounted on your system, install exfat-fuse and exfat-util by typing in your console:

    $ sudo apt-get install exfat-fuse exfat-utils

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
Then to run this you have to simply type:

    $ vagrant up

If you want to setup your own ecosystem from scratch, read and execute the following instructions.


## Create and Setup the Environment

```sh
sudo su -
apt-get update
apt-get install --yes git vim nmap htop wget curl unzip maven openjdk-7-jdk

echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
locale-gen en_US.UTF-8
dpkg-reconfigure locales
```

## Install VirtualBox Guest Additions

```sh
apt-get install linux-headers-generic build-essential dkms
wget http://dlc-cdn.sun.com/virtualbox/4.3.26/VBoxGuestAdditions_4.3.26.iso
mkdir /media/VBoxGuestAdditions
mount -o loop,ro VBoxGuestAdditions_4.3.26.iso /media/VBoxGuestAdditions
sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
rm VBoxGuestAdditions_4.3.26.iso
umount /media/VBoxGuestAdditions
rmdir /media/VBoxGuestAdditions
```

## Install and Setup Database For All Tools

```sh
apt-get install --yes postgresql-9.3
su postgres -
psql
```

```sql
CREATE USER confluence WITH PASSWORD 'confluence';
CREATE DATABASE confluence;
GRANT ALL PRIVILEGES ON DATABASE confluence TO confluence;

CREATE USER jira WITH PASSWORD 'jira';
CREATE DATABASE jira;
GRANT ALL PRIVILEGES ON DATABASE jira TO jira;

CREATE USER sonar WITH PASSWORD 'sonar';
CREATE DATABASE sonar;
GRANT ALL PRIVILEGES ON DATABASE stash TO sonar;

CREATE USER stash WITH PASSWORD 'stash';
CREATE DATABASE stash;
GRANT ALL PRIVILEGES ON DATABASE stash TO stash;
```

## Create New Box

    vagrant package --base ecosystem.local --output ecosystem.box
