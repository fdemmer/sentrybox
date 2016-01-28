# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "private_network", ip: "10.10.10.10"

  config.vm.synced_folder '.', '/vagrant'

  config.vm.provider "virtualbox" do |v|
    v.cpus = 2
    v.memory = "1024"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/site.yml"
    ansible.inventory_path = "provisioning/inventory"
    ansible.host_key_checking = false
  end
end
