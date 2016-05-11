# Vagrant create virtual machine

## English

- Use `Vagrantfile` to store following configuration
- Create virtual machine from the official 32 bits `Ununtu LTS` (Long Time Support) image
- Set the hostname to `ubuntu.local`
- Adjust virtual machine resources according to your computer power:
    - 1 CPU core, 1024 MB RAM (if your computer has around 2 CPU core, 4 GB RAM)
    - 2 CPU core, 4096 MB RAM (if you have more powerfull machine)
- Setup port forwarding
    - 80 -> 8080
    - 443 -> 8443
- Synchronize current directory to `/var/www/host`
- Run machine from `Vagrantfile` and start downloading an `Ubuntu` image

## Polish

- Użyj pliku `Vagrantfile` do przetrzymywania następującej konfiguracji
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji `Ubuntu LTS` (Long Time Support)
- Ustaw hostname na `ubuntu.local`
- Ustaw zasoby przydzielane towjej maszynie wirtialnej w zależności od mocy komputera
    - 1 CPU core, 1024 MB RAM (jeżeli masz około 2 CPU core, 4 GB RAM)
    - 2 CPU core, 4096 MB RAM (jeżeli masz mocniejszą maszynę)
- Ustaw forwarding portów
    - 80 -> 8080
    - 443 -> 8443
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`
- Podnieś maszynę z `Vagrantfile` i rozpocznij pobieranie obrazu `Ubuntu`
