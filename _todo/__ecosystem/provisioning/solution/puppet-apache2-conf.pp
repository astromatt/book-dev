class { 'apache':
    default_vhost => false,
}

apache::vhost { 'insecure.example.com':
    servername => 'insecure.example.com',
    port       => 80,
    docroot    => '/var/www/insecure-example-com',
}

apache::vhost { 'ssl.example.com':
    servername => 'ssl.example.com',
    port       => 443,
    docroot    => '/var/www/ssl-example-com',
    ssl        => true,
    ssl_cert   => '/etc/ssl/ssl-example-com.cert',
    ssl_key    => '/etc/ssl/ssl-example-com.key',
}

file { '/var/www/insecure-example-com/index.html':
    ensure  => 'present',
    replace => 'no',
    content => 'Ehlo World! - Insecure\n',
    mode    => 0644,
}

file { '/var/www/ssl-example-com/index.html':
    ensure  => 'present',
    replace => 'no',
    content => 'Ehlo World! - SSL\n',
    mode    => 0644,
}
