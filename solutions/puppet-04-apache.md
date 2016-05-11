# Instalacja i konfiguracja Apache2 za pomocą Puppet

	$ puppet module install apache
	$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout self-signed.key -out self-signed.cert
	$ cat /etc/puppet/manifests/apache.pp

```puppet
class { 'apache':
	default_vhost => false,
}

# The non-ssl virtual host
apache::vhost { 'insecure.example.com':
	servername => 'insecure.example.com',
	port       => 80,
	docroot    => '/var/www/insecure',
}

# The SSL virtual host at the same domain
apache::vhost { 'ssl.example.com':
	servername => 'ssl.example.com',
	port       => 443,
	docroot    => '/var/www/ssl',
	ssl        => true,
	ssl_cert   => '/etc/ssl/self-signed.cert',
	ssl_key    => '/etc/ssl/self-signed.key',
}

file { '/var/www/insecure.example.com/index.html':
  ensure  => 'present',
  replace => 'no',
  content => '<!DOCTYPE html><html><body>EHLO WORLD - INSECURE</body></html>\n',
  mode    => 0644,
}

file { '/var/www/ssl.example.com/index.html':
  ensure  => 'present',
  replace => 'no',
  content => '<!DOCTYPE html><html><body>EHLO WORLD - SSL</body></html>\n',
  mode    => 0644,
}
```
	$ puppet apply /etc/puppet/manifests/apache.pp
	$ ls /var/www
	$ cat /etc/apache2/sites-enabled/*
