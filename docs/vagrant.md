# Vagrant

## Tworzenie i konfigurowanie maszyny

### Zadanie

- Stwórz maszynę z obrazu ubuntu32lts oficjalnego ze strony Ubuntu
- Ustaw hostname na `ubuntu.local`
- Zrób by maszyna miała 128 MB RAM
- Przydziel maszynie 1 Core
- Zrób by maszyna była stawiana z manifestu Puppeta
- Ustaw forwarding portu 80 na 8080 hosta oraz 443 na 8443
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`

### Rozwiązanie

```Vagrantfile
CPU = 1
RAM = 128

Vagrant.configure("2") do |config|
	config.vm.box = "ubuntu32lts"
	config.vm.hostname = "ubuntu.local"
	config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"
	config.vm.network :forwarded_port, guest: 80, host: 8080
	config.vm.network :forwarded_port, guest: 443, host: 8443
	config.vm.synced_folder ".", "/var/www/host"

	config.vm.provider "virtualbox" do |v|
	    v.name = "ecosystem.local"
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
