exec { 'package definition update':
    command => '/usr/bin/apt update',
}

package { ['nmap', 'htop', 'git']:
    ensure => 'latest',
    require => Exec['package definition update'],
}
