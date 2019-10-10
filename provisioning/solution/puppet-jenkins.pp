group { 'jenkins':
    ensure => 'present',
    gid    => 1337,
}

user { 'jenkins':
    ensure           => 'present',
    groups           => ['jenkins'],
    home             => '/home/jenkins',
    password         => '*',
    password_max_age => 99999,
    password_min_age => 0,
    shell            => '/bin/bash',
    uid              => 1337,
}

file { '/home/jenkins':
    ensure => 'directory',
    owner  => 'jenkins',
    group  => 'jenkins',
    mode   => '0755'
}
