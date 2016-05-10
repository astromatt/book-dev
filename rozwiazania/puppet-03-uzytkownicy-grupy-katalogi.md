```puppet
group { 'www-data':
	ensure => 'present',
	gid    => 33,
}

user { 'www-data':
	ensure           => 'present',
	comment          => 'www-data',
	groups           => ['www-data'],
	home             => '/var/www',
	password         => '*',
	password_max_age => 99999,
	password_min_age => 0,
	shell            => '/usr/sbin/nologin',
	uid              => 33,
}

file { '/var/www':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => 0755
}
```
