# Change hostname

## English

- Create manifest in `/etc/puppet/manifests/hostname.pp`
- Using manifest change the hostname to `ecosystem.local`
- Make sure that command `hostname` returns valid output
- Make sure that `hostname` do not restores to default after reboot

## Polish

- Manifest do tego zadania zapisz w pliku `/etc/puppet/manifests/hostname.pp`
- Za pomocą manifestu zmień hostname maszyny na `ecosystem.local`
- Upewnij się, że po wpisaniu polecenia `hostname` będzie ustawiona na odpowiednią wartość
- Upewnij się, że hostname nie przywróci się do domyślnej wartości po ponownym uruchomieniu
