1874

steps straight from minimal debian, you can edit it as you like especially on the gnome part
after debian minimal installation as root

apt install sudo nala
add youruser to sudo as root

adduser yourusername sudo
choose fastest mirror for nala

sudo nala fetch
install base gnome with nala

sudo nala install gdm3 gnome-shell gnome-terminal gnome-text-editor
install file manager, firefox etc

sudo nala install firefox-esr nautilus nautilus-extension-gnome-terminal ffmpegthumbnailer dconf-editor
enable gui login

sudo systemctl enable gdm && sudo systemctl set-default graphical.target
reboot and login

sudo reboot



[WARNING]: Could not match supplied host pattern, ignoring: dell

ansible-pull -i dell -o -U https://github.com/Vanderbull/ansible.git


https://docs.ansible.com/ansible/latest/collections/community/general/discord_module.html
# install git
sudo apt install git

# install gitfiend
- https://gitfiend.com/

# install codeblocks
- sudo apt install codeblocks
- sudo apt install codeblocks-contrib

# install blender
sudo snap install blender

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
sudo ansible-pull -i hp, -U https://github.com/bjonke/ansible.git

username:
password: <token>

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

---
https://docs.vultr.com/how-to-configure-a-debian-11-bullseye-server-with-ansible
