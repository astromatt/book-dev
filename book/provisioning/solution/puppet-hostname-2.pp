exec { 'set hostname':
    command => '/usr/bin/hostnamectl set-hostname ecosystem.local'
}
