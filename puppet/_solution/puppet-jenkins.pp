group { 'myuser':
    ensure => present,
    gid    => 1337,
}

user { 'myuser':
    ensure           => present,
    groups           => ['mygroup'],
    home             => '/home/myuser',
    password         => '*',
    password_max_age => 99999,
    password_min_age => 0,
    shell            => '/bin/bash',
    uid              => 1337,
}

file { '/home/myuser':
    ensure => 'directory',
    owner  => 'myuser',
    group  => 'mygroup',
    mode   => '0755'
}
