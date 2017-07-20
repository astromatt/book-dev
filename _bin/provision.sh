#!/bin/sh

## Create user vagrant with password vagrant
## Ubuntu LTS xenial do not have this account
## This is against vagrant specification
## However Ubunut did not change that yet

useradd vagrant
(echo vagrant; echo vagrant) |passwd vagrant


## If you're behind the firewall and there is
## a problem with donwloading puppet modules
## because od SSL error, you might want to
## uncomment the following section
## and create on Amazon AWS free tier machine
## with Squid http proxy

# export http_proxy=http://<IP_ADDRESS>:3128
# export https_proxy=https://<IP_ADDRESS>:3128


## Execute following lines after spawning the machine

apt-get update
apt-get install --yes puppet
apt-get install --yes git

