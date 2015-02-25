Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/site.yml"
    ansible.sudo = true
  end
  config.vm.network :forwarded_port, guest: 9000, host: 9000
end
