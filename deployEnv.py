# -*- coding: utf-8 -*-
#!/usr/bin/env python
#quick deploy node.js env and python flask env

import os
import sys
import subprocess
import platform
from subprocess import *

NODEJS_URL = 'http://nodejs.org/dist/v0.10.32/node-v0.10.32.tar.gz'
OPENRESTY_URL = 'http://openresty.org/download/ngx_openresty-1.7.4.1.tar.gz'
MONGODB_URL = 'http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.6.5.tgz'
PERCONA_URL = 'http://www.percona.com/redir/downloads/Percona-Server-5.6/LATEST/source/tarball/percona-server-5.6.21-69.0.tar.gz'
PERCONA_PWD = '123456'
PYTHON27_URL = 'http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz'
PIP_URL = 'https://bootstrap.pypa.io/get-pip.py'


INSTALL_PARENT_FOLDER = '/var'
INSTALL_FOLDER = 'devSoft'
INSTALL_PATH = INSTALL_PARENT_FOLDER+'/'+INSTALL_FOLDER+'/'

#check if is linux
sysPlatform = sys.platform
if sysPlatform.index('linux') == -1:
    print 'This script only support centos6 or centos7, not support %s, sorry.'.format(sysPlatform)
    sys.exit(0)

#check is centos6 or centos7
platformRelease = platform.release()
if platformRelease[0] == '3':
    CENTOS_VERSION = 7
else:
    CENTOS_VERSION = 6

#define print func
def outPutInfo():
    for line in streamObj.stdout.readlines():
        print line







#------------------------------------------------



#
# #yum install software
# streamObj = subprocess.call(['yum install -y gcc gcc-c++ kernel-devel wget'], shell=True)
# streamObj = subprocess.call(['yum install -y cmake readline-devel pcre-devel openssl-devel openssl zlib zlib-devel pcre-devel'], shell=True)
# streamObj = subprocess.call(['yum install -y git'], shell=True)
#
# #mkdir install software folder
# streamObj = subprocess.call(['mkdir {0}'.format(INSTALL_FOLDER)], cwd=INSTALL_PARENT_FOLDER, shell=True)
# streamObj = subprocess.call(['chmod 777 {0}'.format(INSTALL_FOLDER)], cwd=INSTALL_PARENT_FOLDER, shell=True)
#
# #install python2.7.8
# #get python tar
#
# streamObj = subprocess.call(['wget {0}'.format(PYTHON27_URL)],cwd=INSTALL_PATH, shell=True)
# softwareName = os.path.basename(PYTHON27_URL)
# softwarePath = INSTALL_PATH + os.path.splitext(softwareName)[0]
# print(softwarePath)
# streamObj = subprocess.call(['tar -zxvf {0}'.format(softwareName)], cwd=INSTALL_PATH, shell=True)
# streamObj = subprocess.call(['./configure'], cwd=softwarePath, shell=True)
# streamObj = subprocess.call(['make', 'make install'], cwd=softwarePath, shell=True)
#
# #show python version
# streamObj = subprocess.call(['python -V'], shell=True)
#
#
#
#
# #install pip
#
# streamObj = subprocess.call(['wget {0}'.format(PIP_URL)],cwd=INSTALL_PATH, shell=True)
# softwareName = os.path.basename(PIP_URL)
# softwarePath = INSTALL_PATH + softwareName
# print(softwareName)
# #run pip setup
# streamObj = subprocess.call(['chmod 777 {0}'.format(softwarePath)], cwd=INSTALL_PATH, shell=True)
# streamObj = subprocess.call(['python {0}'.format(softwareName)], cwd=INSTALL_PATH, shell=True)
#
# #install python package
# streamObj = subprocess.call(['pip install flask', 'pip install gevent', 'pip install gunicorn'], shell=True)
#
# #create python work directory
# streamObj = subprocess.call(['mkdir python', 'chomd 777 python'],cwd=INSTALL_PARENT_FOLDER, shell=True)
# #show python pip list
# streamObj = subprocess.call(['pip list'], shell=True)













#
#
# #install node.js
# #get nodejs tar
# streamObj = subprocess.call(['wget {0}'.format(NODEJS_URL)], cwd=INSTALL_PATH, shell=True)
#
# softwareName = os.path.basename(NODEJS_URL)
# softwarePath = INSTALL_PATH + os.path.splitext(os.path.splitext(softwareName)[0])[0]
# print(softwarePath)
#
# streamObj = subprocess.call(['tar -zxvf {0}'.format(softwareName)], cwd=INSTALL_PATH, shell=True)
# streamObj = subprocess.call(['./configure'], cwd=softwarePath, shell=True)
# streamObj = subprocess.call(['make'], cwd=softwarePath, shell=True)
# streamObj = subprocess.call(['make install'], cwd=softwarePath, shell=True)
# #show node version
# streamObj = subprocess.call(['node -v', 'npm -v'], cwd=softwarePath, shell=True)
#
# #install pm2
# streamObj = subprocess.call(['npm install -g pm2 --unsafe-perm'],cwd=softwarePath, shell=True)
#
# #create nodejs work directory
# streamObj = subprocess.call(['mkdir nodejs'],cwd=INSTALL_PARENT_FOLDER, shell=True)
#
# streamObj = subprocess.call(['chmod 777 nodejs'],cwd=INSTALL_PARENT_FOLDER, shell=True)
















#install mongodb
#get mongodb
streamObj = subprocess.call(['wget {0}'.format(MONGODB_URL)], cwd=INSTALL_PATH, shell=True)

softwareName = os.path.basename(MONGODB_URL)
softwarePath = INSTALL_PATH + os.path.splitext(softwareName)[0]
print(softwarePath)
streamObj = subprocess.call(['tar -zxvf {0}'.format(softwareName)], cwd=INSTALL_PATH, shell=True)
#soft link commond
streamObj = subprocess.call(['rm -rf /usr/sbin/mongod'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['rm -rf /usr/sbin/mongo'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['rm -rf /usr/sbin/mongodump'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['rm -rf /usr/sbin/mongorestore'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['ln -s {0} /usr/sbin/'.format(softwarePath+'/bin/mongod')],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['ln -s {0} /usr/sbin/'.format(softwarePath+'/bin/mongo')],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['ln -s {0} /usr/sbin/'.format(softwarePath+'/bin/mongodump')],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['ln -s {0} /usr/sbin/'.format(softwarePath+'/bin/mongorestore ')],cwd=INSTALL_PATH, shell=True)

#mkdir folder
streamObj = subprocess.call(['mkdir mongodb_database'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['mkdir mongodb_log'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['chmod 777 mongodb_database'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['mkdir 777 mongodb_log'],cwd=INSTALL_PATH, shell=True)
#start mongodb
streamObj = subprocess.call(['mongod  --dbpath={0} --fork --logpath={1}'.format(INSTALL_PATH+'mongodb_database/', INSTALL_PATH+'mongodb_log/log')], cwd=INSTALL_PATH, shell=True)



if True:
    sys.exit(0)



#install openresty
streamObj = subprocess.call(['wget {0}'.format(OPENRESTY_URL)], cwd=INSTALL_PATH, shell=True)

softwareName = os.path.basename(OPENRESTY_URL)
softwarePath = INSTALL_PATH + os.path.splitext(os.path.splitext(softwareName)[0])[0]

print(softwarePath)
streamObj = subprocess.call(['tar -zxvf {0}'.format(softwareName)], cwd=INSTALL_PATH, shell=True)
#compile
configureParam = '''--prefix=/opt/openresty \
            --with-pcre-jit \
            --with-ipv6 \
            --without-http_redis2_module \
            --with-http_iconv_module \
            -j2'''
streamObj = subprocess.call(['./configure {0}'.format(configureParam)], cwd=softwarePath, shell=True)
streamObj = subprocess.call(['make'], cwd=softwarePath, shell=True)
streamObj = subprocess.call(['make install'], cwd=softwarePath, shell=True)

#soft link commond
streamObj = subprocess.call(['rm -rf /usr/sbin/nginx'], cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['ln -s /opt/openresty/nginx/sbin/nginx /usr/sbin/'], cwd=INSTALL_PATH, shell=True)

#write conf
testServerHost = '''server {
                    listen       80;
                    server_name  www.pytest.com;

                    location / {
                      proxy_pass http://127.0.0.1:5000;
                      proxy_redirect default;
                      proxy_http_version 1.1;
                      proxy_set_header Upgrade $http_upgrade;
                      proxy_set_header Connection $http_connection;
                      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                      proxy_set_header Host $http_host;
                    }
                }'''
f = open('/opt/openresty/nginx/conf/serverHost.conf','w')
f.write(testServerHost+'\n')
f.close()
#start nginx
streamObj = subprocess.call(['nginx'],cwd=softwarePath, shell=True)













#install percona
streamObj = subprocess.call(['wget %s'.format(PERCONA_URL)],cwd=INSTALL_PATH, shell=True)

softwarePathList = PERCONA_URL.split('/')
softwareName = softwarePathList[len(softwarePathList)-1]
softwarePath = INSTALL_PATH + softwareName
print(softwarePath)
streamObj = subprocess.call(['tar -zxvf %s'.format(softwareName)] ,cwd=INSTALL_PATH, shell=True)

configureParam = '''\
  -DCMAKE_BUILD_TYPE:STRING=Release             \
  -DSYSCONFDIR:PATH=/var/mysql                  \
  -DCMAKE_INSTALL_PREFIX:PATH=/var/mysql        \
  -DENABLED_PROFILING:BOOL=ON                   \
  -DENABLE_DEBUG_SYNC:BOOL=OFF                  \
  -DMYSQL_DATADIR:PATH=/var/mysql/data          \
  -DMYSQL_MAINTAINER_MODE:BOOL=OFF              \
  -DWITH_EXTRA_CHARSETS:STRING=utf8,gbk,gb2312  \
  -DWITH_SSL:STRING=bundled                     \
  -DWITH_UNIT_TESTS:BOOL=OFF                    \
  -DWITH_ZLIB:STRING=bundled                    \
  -DWITH_PARTITION_STORAGE_ENGINE:BOOL=ON       \
  -DINSTALL_LAYOUT:STRING=STANDALONE            \
  -DCOMMUNITY_BUILD:BOOL=ON                     \
  -LH'''
streamObj = subprocess.call(['cmake . %s'.format(configureParam)], cwd=softwarePath, shell=True)

streamObj = subprocess.call(['make', 'make install'], cwd=softwarePath, shell=True)

#echo lib
streamObj = subprocess.call(['echo /var/mysql/lib/ >> /etc/ld.so.conf'], cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['echo /var/mysql/lib/plugin >> /etc/ld.so.conf'], cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['ldconfig'], cwd=INSTALL_PATH, shell=True)

#cp conf and service
streamObj = subprocess.call(['cp %s /etc/my.cnf'.format(softwarePath+'/support-files/my-medium.cnf')], cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['cp %s /etc/rc.d/init.d/mysqld'.format(softwarePath+'/support-files/mysql.server')], cwd=INSTALL_PATH, shell=True)

#chmod auth
streamObj = subprocess.call(['chmod 700 /etc/rc.d/init.d/mysqld'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['chkconfig --add mysqld'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['chkconfig --level 345 mysqld on'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['chmod 755 /etc/init.d/mysqld'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['groupadd mysql', 'useradd -g mysql -s /sbin/nologin'],cwd=INSTALL_PATH, shell=True)


#soft link
streamObj = subprocess.call(['rm -rf /usr/sbin/mysql'],cwd=INSTALL_PATH, shell=True)
streamObj = subprocess.call(['ln -s /var/mysql/bin/mysql /usr/sbin/'],cwd=INSTALL_PATH, shell=True)

#set default
streamObj = subprocess.call(['chmod 700 %s'.format(softwarePath+'/scripts/mysql_install_db')],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call([softwarePath+'/scripts/mysql_install_db -defaults-file=/etc/my.cnf --basedir=/var/mysql --user=mysql --datadir=/var/mysql/data'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['chown mysql.mysql -R /var/mysql/'],cwd=INSTALL_PATH, shell=True)

#start mysql
streamObj = subprocess.call(['service mysqld start'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['chmod 700 -r /var/mysql/'],cwd=INSTALL_PATH, shell=True)


#create root auth
mysqlCmd1 = 'grant all on *.* to root@"%" identified by "'+PERCONA_PWD+'";'
mysqlCmd2 = 'FLUSH PRIVILEGES;'
streamObj = subprocess.call(['chown mysql.mysql -R /var/mysql/'], stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True)
streamObj.stdin.write(mysqlCmd1)
streamObj.stdin.write(mysqlCmd2)
streamObj.stdin.write('exit;')



#iptables start
if CENTOS_VERSION == 7:
     #close firewall
    streamObj = subprocess.call(['systemctl disable firewalld'],cwd=INSTALL_PATH, shell=True)
    
    streamObj = subprocess.call(['systemctl stop firewalld'],cwd=INSTALL_PATH, shell=True)
    
    streamObj = subprocess.call(['systemctl mask firewalld'],cwd=INSTALL_PATH, shell=True)
    
    #install iptables
    streamObj = subprocess.call(['yum -y install iptables-services'],cwd=INSTALL_PATH, shell=True)
    
    #add boot
    streamObj = subprocess.call(['systemctl enable iptables'],cwd=INSTALL_PATH, shell=True)
    
    streamObj = subprocess.call(['systemctl start iptables'],cwd=INSTALL_PATH, shell=True)
    

centosIptables = '''
            #!/bin/sh -e

            #----------------------------------------------------------
            # iptables settings
            #----------------------------------------------------------

            #Connection IP address

            #----------------------Standard part---------------------------
            # Stop iptables service first
            #service iptables stop
            /sbin/iptables -F
            /sbin/iptables -X
            /sbin/iptables -Z

            # Inital chains default policy
            /sbin/iptables -F -t filter
            /sbin/iptables -P INPUT DROP
            /sbin/iptables -P OUTPUT ACCEPT

            # Enable Native Network Transfer
            /sbin/iptables -A INPUT -i lo -j ACCEPT

            # Accept Established Connections
            /sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

            # ICMP Control
            /sbin/iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 10 -j ACCEPT


            # SSH Service
            /sbin/iptables -A INPUT  -p tcp --dport 22 -j ACCEPT


            #-----------------------Custom part-----------------------

            # HTTP Service
            /sbin/iptables -A INPUT -p tcp --dport 80 -j ACCEPT

            # mysql Service
            /sbin/iptables -A INPUT -p tcp --dport 3306 -j ACCEPT

            # Games Service
            #/sbin/iptables -A INPUT -p tcp --dport 8681:8683 -j ACCEPT
            #/sbin/iptables -A INPUT -p tcp -m multiport --dport 8706,8708 -j ACCEPT


            #deny all Service
            /sbin/iptables -A INPUT -j REJECT --reject-with icmp-host-prohibited
            /sbin/iptables -A FORWARD -j REJECT --reject-with icmp-host-prohibited

            service iptables save
            '''
#gen iptables file
f = open(INSTALL_PATH+'/iptables.sh','w')
f.write(centosIptables+'\n')
f.close()
#add auth and run
streamObj = subprocess.call(['chmod 777 iptables.sh'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['./iptables.sh'],cwd=INSTALL_PATH, shell=True)

streamObj = subprocess.call(['/usr/libexec/iptables/iptables.init save'],cwd=INSTALL_PATH, shell=True)






