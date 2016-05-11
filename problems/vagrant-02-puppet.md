# Vagrant + Puppet

## English

- Copy manifests from the previous tasks (stored in `/etc/puppet/manifests/*`) to `puppet/manifests/` directory on your local machine
- Copy SSL certificates generated to `ssl/` directory on your local machine
- Power-off machine `vagrant halt` and destroy it `vagrant destroy`
- Edit `Vagrantfile` and modify to provision from `Puppet` manifests
- Do not put any logic to `Vagrantfile` use `Puppet` manifests instead
- Copy SSL certificates from your local computer to the guest machine using `Puppet` (do not generate new certificates!) put the configuration in `puppet/manifests/certificates.pp`
- Use one `puppet/main.pp` to include others manifests from `puppet/manifests/*` - do not put everything in the one file

## Polish

- Skopiuj dotychczasowe manifesty z poprzednich zadań (`/etc/puppet/manifests/*`) na swój komputer do katalogu `puppet/manifests/`
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu `ssl/`
- Wyłącz maszynę `vagrant halt`, a następnie ją usuń `vagrant destroy`
- Edytuj plik `Vagrantfile` i dopisz, by maszyna była stawiana z manifestów `Puppet`
- W pliku `Vagrantfile` trzymaj jak najmniej logiki i wszystko rób za pomocą `Puppet`
- Zrób by certyfikaty były przenoszone z twojego komputera na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą `Puppet`, umieść to w pliku `puppet/manifests/certificates.pp`
- Każdy z manifestów powinien być w osobnych plikach a jeden `puppet/main.pp` powinien includować pozostałe z katalogu `puppet/manifests/*`
