file { [
        '/var/www',
        '/var/www/insecure-example-com',
        '/var/www/ssl-example-com',
    ]:
    ensure => 'directory',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0755',
}


# Alternatywnie, można każdy z katalogów definiować osobno

file {'/var/www':
    ensure => 'directory',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0755',
}

file {'/var/www/insecure-example-com':
    ensure => 'directory',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0755',
}

file {'/var/www/ssl-example-com':
    ensure => 'directory',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0755',
}
