# Vagrant create virtual machine

## English

- Use `Vagrantfile` to store following configuration
- Create virtual machine from the official 32 bits `Ununtu LTS` (Long Time Support) image
- Set the hostname to `ubuntu.local`
- Adjust virtual machine resources according to your computer power:
    - 1 CPU core, 1024 MB RAM (if your computer has around 2 CPU core, 4 GB RAM)
    - 2 CPU core, 8196 MB RAM (if you have more powerfull machine)
- Setup port forwarding
    - 80 -> 8888
    - 443 -> 8443
    - 7990 -> 7990
    - 7999 -> 7999
    - 8080 -> 8080
    - 8081 -> 8081
    - 8090 -> 8090
    - 9000 -> 9000
    - 5432 -> 5432
    - 3306 -> 3306
- Synchronize current directory to `/var/www/host`
- Run machine from `Vagrantfile` and start downloading an `Ubuntu` image

## Polish

- Użyj pliku `Vagrantfile` do przetrzymywania następującej konfiguracji
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji `Ubuntu LTS` (Long Time Support)
- Ustaw hostname na `ubuntu.local`
- Ustaw zasoby przydzielane towjej maszynie wirtialnej w zależności od mocy komputera
    - 1 CPU core, 1024 MB RAM (jeżeli masz około 2 CPU core, 4 GB RAM)
    - 2 CPU core, 8196 MB RAM (jeżeli masz mocniejszą maszynę)
- Ustaw forwarding portów
    - 80 -> 8888
    - 443 -> 8443
    - 7990 -> 7990
    - 7999 -> 7999
    - 8080 -> 8080
    - 8081 -> 8081
    - 8090 -> 8090
    - 9000 -> 9000
    - 5432 -> 5432
    - 3306 -> 3306
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`
- Podnieś maszynę z `Vagrantfile` i rozpocznij pobieranie obrazu `Ubuntu`
