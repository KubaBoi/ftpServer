# FTP server

## Install

python -m pip install -U pip setuptools

pip install pyftpdlib

firewall-cmd --zone=public --permanent --add-port=21/tcp --permanent

firewall-cmd --zone=public --permanent --add-port=60000-60099/tcp --permanent

firewall-cmd --zone=public --permanent --add-service=ftp

firewall-cmd --reload