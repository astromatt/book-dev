# Puppet Apache2 installation

## English

- Create manifest in `/etc/puppet/manifests/apache.pp`
- Install and confugure `Apache 2` using `Puppet` module
- Using terminal generate self-signed OpenSSL certificates and put them in `/etc/ssl/`
    - `/etc/ssl/ssl.example.com.cert`
    - `/etc/ssl/ssl.example.com.key`
- Using `Puppet` create two vhosts
    - `insecure.example.com` using port `80` and with document root in `/var/www/insecure.example.com`
    - `ssl.example.com` using port `443` with document root in `/var/www/ssl.example.com` using certificates from `/etc/ssl/`
- Create file:
    - `/var/www/insecure.example.com/index.html` with content `Ehlo World!`
    - `/var/www/ssl.example.com/index.html` with content `Ehlo SSL!`
- Run browser on your localhost:
    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

## Polish

- Manifest do tego zadania zapisz w pliku `/etc/puppet/manifests/apache.pp`
- Zainstaluj i skonfiguruj `Apache 2` wykorzystując moduł `Puppet`
- Z terminala wygeneruj certyfikaty self signed OpenSSL (`.cert` i `.key`) i umieść je w `/etc/ssl/`
- Za pomocą `Puppet` stwórz dwa vhosty
    - `insecure.example.com` na porcie `80` i z katalogiem domowym `/var/www/insecure.example.com`
    - `ssl.example.com` na porcie `443` i z katalogiem domowym `/var/www/ssl.example.com` + używanie certyfikatów SSL wcześniej wygenerowanych
- Stwórz pliki z treścią:
    - `/var/www/insecure.example.com/index.html` z treścią `Ehlo World!`
    - `/var/www/ssl.example.com/index.html` z treścią `Ehlo SSL!`
- W przeglądarce na komputerze lokalnym wejdź na stronę:
    - http://127.0.0.1:8080
    - https://127.0.0.1:8443
