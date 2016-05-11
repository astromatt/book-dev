# Automatyzacja stawiania Vagrant + Puppet
- Skopiuj dotychczasowe manifesty puppeta na swój komputer do katalogu `puppet/manifests/`
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu `conf/ssl/`
- Wyłącz maszynę z Vagrantem `vagrant halt` a następnie ją usuń `vagrant destroy`
- Edytuj plik `Vagrantfile` i dopisz, by maszyna była stawiana z manifestów Puppeta
- W pliku `Vagrantfile` trzymaj jak najmniej logiki i wszystko rób za pomocą Puppeta
- Zrób by certyfikaty były przenoszone z Twojego laptopa na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą Puppeta
- Każdy z manifestów powinien być w osobnych plikach a jeden `main.pp` powinien includować pozostałe
