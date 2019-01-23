exec { 'package definition update':
  command => '/usr/bin/apt-get update';
}

Exec['package definition update'] -> Package <| |>

package { ['htop', 'nmap', 'git']:
  ensure => present;
}
