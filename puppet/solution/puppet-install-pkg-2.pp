Exec { 'package definition update':
  command => '/usr/bin/apt update',
}

package { 'htop':
    ensure => 'latest',
}

package { 'nmap':
    ensure => 'latest',
}

package { 'git':
    ensure => 'latest',
}
