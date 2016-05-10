# Instalacja pakietów za pomocą Puppet

    $ cat /etc/puppet/manifests/packages.pp

## Rozwiązanie 1

```puppet
exec { 'package definition update':
	command => '/usr/bin/apt-get update',
}

package { ['nmap', 'htop', 'git']:
	ensure	=> 'latest',
	require => Exec['package definition update'],
}
```

## Rozwiązanie 2

```puppet
exec { 'package definition update':
  command => '/usr/bin/apt-get update';
}

Exec['package definition update'] -> Package <| |>

package { ['htop', 'nmap', 'git']:
  ensure => present;
}
```

## Rozwiązanie 3

```puppet
exec { 'package definition update':
  command => '/usr/bin/apt-get update',
}

Exec['package definition update'] -> Package <| |>

package { 'htop':
	ensure => 'latest',
}

package { 'nmap':
	ensure => 'latest',
}

package { 'git':
	ensure => 'latest',
}
```
