# Vagrant

## Tworzenie i konfigurowanie maszyny

### Zadanie

- Poniższe polecenia wykonaj w pliku Vagrantfile
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji Ubuntu LTS (Long Time Support)
- Ustaw hostname na `ubuntu.local`
- Jeżeli masz słabszą maszynę (2 CPU core, 4 GB RAM):
	- 1 CPU core
	- 1024 MB Ram
- Jeżeli masz lepszy komputer:
	- 2 CPU core
	- 4096 MB RAM
- Ustaw forwarding portu 80 na 8080 hosta oraz 443 na 8443
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`
- Zrób by maszyna była stawiana z manifestu Puppeta
- Podnieś maszynę i rozpocznij pobieranie obrazu

### Rozwiązanie

	$ vagrant init ubuntu/trusty32

```Vagrantfile
CPU = 1
RAM = 1024

Vagrant.configure("2") do |config|
	config.vm.box = "ubuntu32lts"
	#config.vm.box = "ubuntu/trusty32"
	config.vm.hostname = "ubuntu.local"
	config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"
	config.vm.network :forwarded_port, guest: 80, host: 8080
	config.vm.network :forwarded_port, guest: 443, host: 8443
	config.vm.synced_folder ".", "/var/www/host"

	config.vm.provider "virtualbox" do |v|
	    v.name = "ubuntu.local"
	    v.cpus = CPU
		v.memory = RAM
	end

	config.vm.provision :puppet do |puppet|
		puppet.manifests_path = "puppet/manifests"
		puppet.manifest_file = "site.pp"
		puppet.module_path = "puppet/modules"
	end
end
```

	$ vagrant up
