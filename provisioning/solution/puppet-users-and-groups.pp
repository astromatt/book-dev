group { 'vagrant':
    ensure => 'present',
    gid    => 13 37,
}

user { 'vagrant':
    ensure           => 'present',
    groups           => ['vagrant'],
    home             => '/home/vagrant',
    password         => '*',
    password_max_age => 99999,
    password_min_age => 0,
    shell            => '/usr/sbin/nologin',
    uid              => 1337,
}

file { '/var/www':
    ensure => 'directory',
    owner  => 'vagrant',
    group  => 'vagrant',
    mode   => 0755
}
