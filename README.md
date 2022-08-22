# FTP server

## Install

python -m pip install -U pip setuptools

pip install pyftpdlib

## Centos ftp

sudo yum install vsftpd

sudo systemctl start vsftpd

sudo systemctl enable vsftpd

firewall-cmd --zone=public --permanent --add-port=21/tcp

firewall-cmd --zone=public --permanent --add-service=ftp

firewall-cmd --reload

### Config

sudo cp /etc/vsftpd/vsftpd.conf /etc/vsftpd/vsftpd.conf.default

sudo nano /etc/vsftpd/vsftpd.conf

```python
anonymous_enable=NO

local_enable=YES

write_enable=YES

chroot_local_user=YES

allow_writeable_chroot=YES

userlist_enable=YES

userlist_file=/etc/vsftpd/user_list

userlist_deny=NO
```

sudo systemctl restart vsftpd

### add user

sudo adduser kuba

sudo passwd kuba

password = Heslo_12

echo “kuba” | sudo tee –a /etc/vsftpd/user_list

sudo mkdir –p /home/kuba/ftp/upload

sudo chmod 550 /home/kuba/ftp

sudo chmod 750 /home/kuba/ftp/upload

sudo chown –R kuba: /home/kuba/ftp

### Connect

ftp 192.168.01