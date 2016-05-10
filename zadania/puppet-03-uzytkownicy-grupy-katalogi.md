# Zarządzanie użytkownikami, grupami i katalogami
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/www-data.pp`
- Za pomocą Puppet upewnij się by był użytkownik `www-data` i miał `uid=33`
- Za pomocą Puppet upewnij się by była grupa `www-data` i miała `gid=33`
- Upewnij się że katalog `/var/www` istnieje i właścicielem jego są user `www-data` i grupa `www-data` i że ma uprawnienia `rwxr-xr-x`
