## Adjust your settings here

CPU = 2
RAM = 8196


################################
# Do not modify anything below #
################################

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty32"

	# config.vm.box = "ecosystem.box"
    # config.vm.box = "ubuntu32lts"
    # config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

    config.vm.host_name = "ecosystem.local"

    config.vm.network :forwarded_port, guest: 80, host: 8888
    config.vm.network :forwarded_port, guest: 443, host: 8443
    config.vm.network :forwarded_port, guest: 7990, host: 7990
    config.vm.network :forwarded_port, guest: 7999, host: 7999
    config.vm.network :forwarded_port, guest: 8080, host: 8080
    config.vm.network :forwarded_port, guest: 8081, host: 8081
    config.vm.network :forwarded_port, guest: 8090, host: 8090
    config.vm.network :forwarded_port, guest: 9000, host: 9000
    config.vm.network :forwarded_port, guest: 3306, host: 3306
    config.vm.network :forwarded_port, guest: 5432, host: 5432
    config.vm.synced_folder ".", "/var/www/src/"

    config.vm.provider "virtualbox" do |v|
        v.name = "ecosystem.local"
        v.cpus = CPU
        v.memory = RAM
    end

end

