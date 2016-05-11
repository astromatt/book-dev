# Change hostname

    $ cat /etc/puppet/manifests/hostname.pp

## Method 1

```puppet
file { "/etc/hostname":
        ensure  => present,
        owner   => root,
        group   => root,
        mode    => '0644',
        content => "ecosystem.local\n",
        notify  => Exec["set hostname"],
}

exec { "set hostname":
        command => '/bin/hostname -F /etc/hostname',
        unless  => "/usr/bin/test `hostname` = `/bin/cat /etc/hostname`",
}
```

## Method 2

```puppet
exec { 'set hostname':
	command => '/usr/bin/hostnamectl set-hostname ecosystem.local'
}
```
