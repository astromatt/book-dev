# Users, Groups and Directories management

```puppet
group { 'mygroup':
	ensure => 'present',
	gid    => 99,
}

user { 'myuser':
	ensure           => 'present',
	groups           => ['mygroup'],
	home             => '/home/myuser',
	password         => '*',
	password_max_age => 99999,
	password_min_age => 0,
	shell            => '/usr/sbin/nologin',
	uid              => 1337,
}

file { '/var/www':
  ensure => 'directory',
  owner  => 'myuser',
  group  => 'mygroup',
  mode   => 0755
}
```
