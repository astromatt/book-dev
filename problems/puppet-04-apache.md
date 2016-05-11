# Instalacja i konfiguracja Apache2 za pomocą Puppet

- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/apache.pp`
- Zainstaluj i skonfiguruj Apache2 wykorzystując moduł Puppet
- Z terminala wygeneruj certyfikaty self signed OpenSSL (`.cert` i `.key`) (za pomocą i umieść je w `/etc/ssl/`)
- Za pomocą Puppet Stwórz dwa vhosty
    - `insecure.example.com` na porcie 80 i z katalogiem domowym `/var/www/insecure.example.com`
    - `ssl.example.com` na porcie 443 i z katalogiem domowym `/var/www/ssl.example.com` + używanie certyfikatów SSL wcześniej wygenerowanych
- Stwórz pliki z treścią:
    - `/var/www/insecure.example.com/index.html` z treścią `Ehlo World!`
    - `/var/www/ssl.example.com/index.html` z treścią `Ehlo SSL!`
- W przeglądarce na laptopie wejdź na stronę:
    - http://127.0.0.1:8080
    - https://127.0.0.1:8443
