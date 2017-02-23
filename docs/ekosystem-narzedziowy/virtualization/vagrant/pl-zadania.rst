Zadania
-------

Automatyzacja tworzenia wirtualnej maszyny
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Użyj pliku ``Vagrantfile`` do przetrzymywania następującej konfiguracji
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji `Ubuntu LTS` (Long Time Support)
- Ustaw hostname na ``ubuntu.local``
- Ustaw zasoby przydzielane towjej maszynie wirtialnej w zależności od mocy komputera:

    - 1 CPU core, 1024 MB RAM (jeżeli masz około 2 CPU core, 4 GB RAM)
    - 2 CPU core, 8196 MB RAM (jeżeli masz mocniejszą maszynę)

- Ustaw forwarding portów:

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

- Ustaw aby ten katalog był synchronizowany na maszynie gościa w ``/var/www/host``
- Podnieś maszynę z ``Vagrantfile`` i rozpocznij pobieranie obrazu `Ubuntu`


Vagrant + Puppet
^^^^^^^^^^^^^^^^

- Skopiuj dotychczasowe manifesty z poprzednich zadań (``/etc/puppet/manifests/*``) na swój komputer do katalogu ``puppet/manifests/``
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu ``ssl/``
- Wyłącz maszynę ``vagrant halt``, a następnie ją usuń ``vagrant destroy``
- Edytuj plik ``Vagrantfile`` i dopisz, by maszyna była stawiana z manifestów `Puppet`
- W pliku ``Vagrantfile`` trzymaj jak najmniej logiki i wszystko rób za pomocą `Puppet`
- Zrób by certyfikaty były przenoszone z twojego komputera na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą `Puppet`, umieść to w pliku ``puppet/manifests/certificates.pp``
- Każdy z manifestów powinien być w osobnych plikach a jeden ``puppet/main.pp`` powinien includować pozostałe z katalogu ``puppet/manifests/*``



