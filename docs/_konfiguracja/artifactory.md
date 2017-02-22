# Artifactory

```sh
useradd artifactory
cd /opt/
wget http://dl.bintray.com/jfrog/artifactory/artifactory-3.3.1.zip
unzip artifactory-3.3.1.zip
rm -fr artifactory-3.3.1.zip
chown -R artifactory:artifactory artifactory-3.3.1/
cd artifactory-3.3.1/bin/
su artifactory
screen
./artifactory.sh
(detach screen)
```
