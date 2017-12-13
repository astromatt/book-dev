#!/usr/bin/env python2

from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm
from fabric.tasks import Task
from datetime import datetime


class CloneTask(Task):
    name = "clone"
    origin_user = None
    origin_host = None
    clone_user = None
    clone_host = None

    def run(self):
        timestamp_start = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(yellow("[%s] Starting executing jobs..." % timestamp_start))
        execute(self.ask_user)
        execute(self.env_create)
        execute(self.env_rsync)
        execute(self.env_install)
        execute(self.deb_install)
        execute(self.jdk_rsync)
        execute(self.jdk_install)
        execute(self.clitools_rsync)
        execute(self.clitools_install)
        execute(self.preinstall)
        execute(self.install)
        execute(self.postinstall)
        timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(yellow("[%s] Everything done." % timestamp_end))

    def ask_user(self):
        self.origin_user = prompt('What is the origin user?', default=self.origin_user, validate=r'^(\w+)$')
        self.origin_host = prompt('What is the origin host address?', default=self.origin_host)
        self.clone_user = prompt('What is the clone user?', default=self.clone_user, validate=r'^(\w+)$')
        self.clone_host = prompt('What is the clone host address?', default=self.clone_host)
        env.roledefs['origin'] = ["%s@%s" % (self.origin_user, self.origin_host)]
        env.roledefs['clone'] = ["%s@%s" % (self.clone_user, self.clone_host)]
        print("Origin: %s\nClone: %s" % (env.roledefs['origin'], env.roledefs['clone']))
        if not confirm("Continue with this settings?", default=False):
            abort("Aborting at user request.")

    @roles('origin')
    def get_ssh_pubkey(slef):
        print(green("Getting ssh pubkey from origin host..."))
        return sudo('cat /root/.ssh/id_rsa.pub')

    @roles('clone')
    def env_create(self):
        ssh_pubkey = execute(self.get_ssh_pubkey).popitem()[1]
        print(green("Creating Environment..."))
        sudo('mkdir -p /home/%s/.ssh' % self.clone_user)
        sudo('mkdir -p /opt/java')
        sudo('mkdir -p /opt/clitools')
        sudo('echo "%s" >> /home/%s/.ssh/authorized_keys' % (ssh_pubkey, self.clone_user))
        sudo('echo \'export PS1="[\u@\[$(tput bold)\]\[$(tput setaf 1)\]\h\[$(tput sgr0)\]:\w\$] "\' >> /root/.bashrc')
        sudo('chown -R %s /home/%s' % (self.clone_user, self.clone_user))
        sudo('chown -R %s /opt/java' % self.clone_user)
        sudo('chown -R %s /opt/clitools' % self.clone_user)
        sudo('echo "nameserver 8.8.8.8" >> /etc/resolvconf/resolv.conf.d/head')
        sudo('echo "nameserver 8.8.6.6" >> /etc/resolvconf/resolv.conf.d/head')
        sudo('resolvconf -u')

    @roles('origin')
    def env_rsync(self):
        sudo('rsync -raz --delete /etc/environment %s:/tmp/environment' % env.roledefs['clone'][0])

    @roles('clone')
    def env_install(self):
        sudo('mv /tmp/environment /etc/environment')
        sudo('chown root:root /etc/environment')

    @roles('clone')
    def deb_install(self):
        print(green("Installing deb..."))
        sudo('curl http://repo.varnish-cache.org/debian/GPG-key.txt | sudo apt-key add -')
        sudo('echo "deb http://repo.varnish-cache.org/ubuntu/ precise varnish-3.0" | sudo tee -a /etc/apt/sources.list')
        sudo('apt-get --quiet update')
        sudo('DEBIAN_FRONTEND=noninteractive apt-get --quiet --yes install mysql-server')
	sudo('''sed -i -r -b "N;s/\[mysqld\]\\n#/\[mysqld\]\\ninnodb_file_per_table\\nmax_allowed_packet=1024M/g" /etc/mysql/my.cnf''')
        sudo('service mysql restart')
        sudo('apt-get install --quiet --yes varnish')
        sudo('apt-get install --quiet --yes htop')
        sudo('apt-get install --quiet --yes memcached')
        sudo('apt-get install --quiet --yes libmemcached-dev')
        sudo('apt-get install --quiet --yes wget')
        sudo('apt-get install --quiet --yes libxml2-utils')
        sudo('apt-get install --quiet --yes curl')
        sudo('apt-get install --quiet --yes git')
        sudo('apt-get install --quiet --yes nmap')
        sudo('apt-get install --quiet --yes gcc')
        sudo('apt-get install --quiet --yes python-pip')
        sudo('apt-get install --quiet --yes python-virtualenv')
        sudo('apt-get install --quiet --yes libsasl2-dev')
        sudo('apt-get install --quiet --yes python-dev')
        sudo('apt-get install --quiet --yes libldap2-dev')
        sudo('apt-get install --quiet --yes libmysqld-dev')
        sudo('apt-get install --quiet --yes mc')

    @roles('origin')
    def jdk_rsync(self):
        print(green("Rsyncing jdk..."))
        sudo('rsync -raz --delete /opt/java/ %s:/opt/java' % env.roledefs['clone'][0])

    @roles('clone')
    def jdk_install(self):
        print(green("Installing jdk..."))
        sudo('update-alternatives --install /usr/bin/java java /opt/java/default/bin/java 1')
        sudo('update-alternatives --set java /opt/java/default/bin/java')
        sudo('chown -R root:root /opt/java')

    @roles('origin')
    def clitools_rsync(self):
        print(green("Installing clitools..."))
        sudo('rsync -raz --delete /opt/clitools/ %s:/opt/clitools' % env.roledefs['clone'][0])

    @roles('clone')
    def clitools_install(self):
        sudo('chown -R root:root /opt/clitools')

    def preinstall(self):
        raise NotImplementedError

    def install(self):
        raise NotImplementedError

    def postinstall(self):
        raise NotImplementedError


class UpdateTask(Task):
    name = "update"
    origin_user = None
    origin_host = None
    clone_user = None
    clone_host = None

    def run(self):
        timestamp_start = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(yellow("[%s] Starting executing jobs..." % timestamp_start))
        execute(self.ask_user)
        execute(self.jdk_rsync)
        execute(self.preinstall)
        execute(self.install)
        execute(self.postinstall)
        timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(yellow("[%s] Everything done." % timestamp_end))

    def ask_user(self):
        self.origin_user = prompt('What is the origin user?', default=self.origin_user, validate=r'^(\w+)$')
        self.origin_host = prompt('What is the origin host address?', default=self.origin_host)
        self.clone_user = prompt('What is the clone user?', default=self.clone_user, validate=r'^(\w+)$')
        self.clone_host = prompt('What is the clone host address?', default=self.clone_host)
        env.roledefs['origin'] = ["%s@%s" % (self.origin_user, self.origin_host)]
        env.roledefs['clone'] = ["%s@%s" % (self.clone_user, self.clone_host)]
        print("Origin: %s\nClone: %s" % (env.roledefs['origin'], env.roledefs['clone']))
        if not confirm("Continue with this settings?", default=False):
            abort("Aborting at user request.")

    @roles('origin')
    def jdk_rsync(self):
        print(green("Rsyncing jdk..."))
        sudo('rsync -raz --delete /opt/java/ %s:/opt/java' % env.roledefs['clone'][0])

    def preinstall(self):
        raise NotImplementedError

    def install(self):
        raise NotImplementedError

    def postinstall(self):
        raise NotImplementedError


"""
.. todo:
   * Add consolidate DeleteProjects.* to this module
   * Add dry-run option
"""


class Clone(CloneTask):
    name = "clone"
    origin_user = None
    origin_host = "localhost"
    clone_user = "ubuntu"
    clone_host = None

    @roles('clone')
    def preinstall(self):
        print(green("Configuring preinstall actions..."))
        with settings(warn_only=True):
            sudo('useradd --system jira')
        sudo('mkdir -p /opt/jira')
        sudo('chown -R %s /opt/jira' % self.clone_user)

    @roles('origin')
    def install(self):
        print(green("Rsyncing..."))
        clone = env.roledefs['clone'][0]
        exclude = [
            "home/caches/*",
            "home/data/attachments/*",
            "home/export/*",
            "home/import/*",
            "home/log/*",
            "home/tmp/*",
            "*/logs/*",
            "*/jre/*",
	    "home/plugins/.bundled-plugins/*",
	    "*/temp/*",
	    "home/plugins/.osgi-plugins"]
        sudo('rsync -raz --delete --exclude=%(exclude)s /opt/jira/ %(clone)s:/opt/jira' % {
            "clone": clone,
            "exclude": " --exclude=".join(exclude)})
        sudo('rsync -raz --delete /etc/init.d/jira %s:/opt/jira/initd.sh' % clone)

    @roles('clone')
    def postinstall(self):
        print(green("Configuring postinstall actions..."))
        sudo('sed -i "s/localhost/127.0.0.1/g" /opt/jira/home/dbconfig.xml')
        sudo('mysql -e "drop database if exists jira;"')
        sudo('mysql -e "create database jira /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;"')
        sudo('mysql -e "create user jira@localhost identified by \'jira\';"')
        sudo('mysql -e "grant all privileges on jira.* to jira@localhost identified by \'jira\';"')
        sudo('mysqldump -hlocalhost -ujira -p"jira" --lock-all-tables jira |mysql jira')
        sudo('mysql -e "delete from jira.filtersubscription";')
        sudo('mysql -e "delete from jira.mailserver";')
        sudo('mysql -e "update jira.propertystring set propertyvalue=\'http://%s:8080\' where id in (select id from jira.propertyentry where property_key like \'%%baseurl%%\');"' % env.roledefs['clone'][0].split('@')[1])
        sudo('mysql -e "update jira.cwd_user set credential=\'x61Ey612Kl2gpFL56FT9weDnpSo4AV8j8+qx2AuTHdRyY036xxzTTrw10Wq3+4qQyB+XURPWx1ONxp3Y3pB37A==\' where user_name=\'admin\';"')
	sudo('mysql -e "update jira.propertytext set propertyvalue=\'<h3>This is a JIRA test instance</h3>\' where ID=\'11216\';"')
        sudo('date > /opt/jira/database_lastupdate')
        sudo('''sed -i 's/JVM_MINIMUM_MEMORY=".*"/JVM_MINIMUM_MEMORY="256M"/g' /opt/jira/install/bin/setenv.sh''')
        sudo('''sed -i 's/JVM_MAXIMUM_MEMORY=".*"/JVM_MAXIMUM_MEMORY="768M"/g' /opt/jira/install/bin/setenv.sh''')
        sudo('''sed -i 's/scheme="https"//g' /opt/jira/install/conf/server.xml''')
        sudo('''sed -i 's/proxyName="localhost"//g' /opt/jira/install/conf/server.xml''')
        sudo('''sed -i 's/proxyPort="443"//g' /opt/jira/install/conf/server.xml''')
        sudo('echo "jira.autoexport=false" >> /opt/jira/home/jira-config.properties')
        sudo('mv /opt/jira/initd.sh /etc/init.d/jira')
        sudo('chown root:root /etc/init.d/jira')
        sudo('chmod +x /etc/init.d/jira')
        sudo('chown -R jira:jira /opt/jira')
        print(red('/etc/init.d/jira start'))
        print(red('sleep 240 && /opt/jira/home/reindex.sh'))


class Update(UpdateTask):
    name = "update"

    @roles('clone')
    def preinstall(self):
        print(green("Configuring preinstall actions..."))
        sudo('/etc/init.d/jira stop')
        sudo('chown -R %s /opt/jira' % self.clone_user)

    @roles('origin')
    def install(self):
        print(green("Rsyncing..."))
        clone = env.roledefs['clone'][0]
        exclude = [
            "home/caches/*",
            "home/data/attachments/*",
            "home/export/*",
            "home/import/*",
            "home/log/*",
            "home/tmp/*",
            "*/logs/*",
            "*/jre/*",
	    "home/plugins/.bundled-plugins/*",
            "*/temp/*",
            "home/plugins/.osgi-plugins"]
        sudo('rsync -raz --delete --exclude=%(exclude)s /opt/jira/ %(clone)s:/opt/jira' % {
            "clone": clone,
            "exclude": " --exclude=".join(exclude)})
        sudo('rsync -raz --delete /etc/init.d/jira %s:/opt/jira/initd.sh' % clone)

    @roles('clone')
    def postinstall(self):
        print(green("Configuring postinstall actions..."))
        sudo('sed -i "s/localhost/127.0.0.1/g" /opt/jira/home/dbconfig.xml')
        print(red('mysql -e "drop database if exists jira;"'))
        print(red('mysql -e "create database jira /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;"'))
        print(red('mysql -e "grant all privileges on jira.* to jira@localhost identified by \'localhost\';"'))
        print(red('mysqldump -hlocalhost -ujira -p"jira" --lock-all-tables jira |mysql jira'))
        print(red('mysql -e "delete from jira.filtersubscription";'))
        print(red('mysql -e "delete from jira.mailserver";'))
        print(red('mysql -e "update jira.propertystring set propertyvalue=\'http://%s:8080\' where id in (select id from jira.propertyentry where property_key like \'%%baseurl%%\');"' % env.roledefs['clone'][0].split('@')[1]))
        print(red('mysql -e "update jira.cwd_user set credential=\'x61Ey612Kl2gpFL56FT9weDnpSo4AV8j8+qx2AuTHdRyY036xxzTTrw10Wq3+4qQyB+XURPWx1ONxp3Y3pB37A==\' where user_name=\'admin\';"'))
	print(red('mysql -e "update jira.propertytext set propertyvalue=\'<h3>This is a JIRA test instance</h3>\' where ID=\'11216\';"'))
        sudo('date > /opt/jira/database_lastupdate')
        sudo('''sed -i 's/JVM_MINIMUM_MEMORY=".*"/JVM_MINIMUM_MEMORY="256M"/g' /opt/jira/install/bin/setenv.sh''')
        sudo('''sed -i 's/JVM_MAXIMUM_MEMORY=".*"/JVM_MAXIMUM_MEMORY="768M"/g' /opt/jira/install/bin/setenv.sh''')
        sudo('''sed -i 's/scheme="https"//g' /opt/jira/install/conf/server.xml''')
        sudo('''sed -i 's/proxyName="localhost"//g' /opt/jira/install/conf/server.xml''')
        sudo('''sed -i 's/proxyPort="443"//g' /opt/jira/install/conf/server.xml''')
        sudo('mv /opt/jira/initd.sh /etc/init.d/jira')
        sudo('chown root:root /etc/init.d/jira')
        sudo('chown -R jira:jira /opt/jira')
        sudo('chmod +x /etc/init.d/jira')
        print(red('/etc/init.d/jira start'))
        print(red('sleep 240'))
        print(red('/opt/jira/home/reindex.sh'))

clone = Clone()
update = Update()