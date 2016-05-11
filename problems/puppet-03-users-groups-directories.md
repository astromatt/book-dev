# Users, Groups and Directories management

## English

- Create manifest in `/etc/puppet/manifests/users.pp`
- Make sure user `myuser` exists and has `uid=1337`
- Make suer group `mygroup` exists and has `gid=99`
- Make sure:
    - Directory `/var/www` exists
    - Owner is set to `myuser`
    - Group is set to `mygroup`
    - Has `rwxr-xr-x` permissions

## Polish

- Manifest do tego zadania zapisz w pliku `/etc/puppet/manifests/users.pp`
- Upewnij się, że użytkownik `myuser` istnieje i ma `uid=1337`
- Upewnij się, że grupa `mygroup` istnieje i ma `gid=99`
- Upewnij się, że:
    - Katalog `/var/www` istnieje
    - Właścicielem jego jest user `myuser`
    - Właścicielem jego jest grupa `mygroup`
    - Ma uprawnienia `rwxr-xr-x`
