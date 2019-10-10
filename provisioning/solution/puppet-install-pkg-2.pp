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
