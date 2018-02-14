# -*- mode: ruby -*-
# vi: set ft=ruby

VAGRANTFILE_API_VERSION = "2"
BOX_NAME = ENV['VAGRANT_BOX_NAME'] || "bento/centos-7.4"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "nginx" do |nginx|
        nginx.vm.box = BOX_NAME
        nginx.vm.hostname = "nginx-ldap-auth"
        nginx.vm.network :private_network, ip: "192.168.10.10"

        nginx.vm.provision "ansible" do |ansible|
            ansible.playbook = "ansible/install.yml"
        end
    end

    config.vm.provider "virtualbox" do |vbox|
        vbox.name = "nginx-ldap-auth"
        vbox.memory = 2048
        vbox.cpus = 2
    end
end