# Download and install picoCAD
https://johanpeitz.itch.io/picocad

# Installation of Discord
sudo apt install discord

# Installation of steam
sudo apt install steam

# Get support for exFAT instead of FAT
sudo apt-get install exfat-fuse exfat-utils

# ansible
Ansible lab

https://opensource.com/article/18/3/manage-workstation-ansible

sudo apt install ansible

https://kbroman.org/github_tutorial/pages/first_time.html

git clone https://github.com/bjonke/ansible.git

The default location for inventory is a file called /etc/ansible/hosts

#Trailing , important for workaround to work
sudo ansible-pull -i dumbo, -U https://github.com/bjonke/ansible.git

https://medium.com/@perwagnernielsen/ansible-tutorial-part-2-installing-packages-41d3ab28337d

ansible localhost -m ping

ansible-playbook --connection=local --inventory 127.0.0.1, gnome-todo.yml -i hosts

Show a history of recently installed packages, their version number, and the date / time they were installed on Debian, Ubuntu or Linux Mint:

grep "install " /var/log/dpkg.log

Show a history of recently removed packages and the date / time they were removed, on Debian, Ubuntu or Linux Mint:

grep "remove " /var/log/dpkg.log


apt list --installed

apt -qq list program_name --installed

update-desktop-database
