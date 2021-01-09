puppet module install puppetlabs-apache
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/ssl-example-com.key -out /etc/ssl/ssl-example-com.cert
cat /etc/puppet/manifests/apache.pp
