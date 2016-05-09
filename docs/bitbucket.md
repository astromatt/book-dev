# Bitbucket

## Install

    wget https://www.atlassian.com/software/stash/downloads/binary/atlassian-stash-3.8.0-x64.bin
    chmod +x atlassian-stash-3.8.0-x64.bin
    ./atlassian-stash-3.8.0-x64.bin
    rm -fr atlassian-stash-3.8.0-x64.bin

## Install using Docker

	docker pull atlassian/bitbucket-server

    docker run -u root -v /data/bitbucket:/var/atlassian/application-data/bitbucket atlassian/bitbucket-server chown -R daemon  /var/atlassian/application-data/bitbucket

    docker run -v /data/bitbucket:/var/atlassian/application-data/bitbucket --name="bitbucket" -d -p 7990:7990 -p 7999:7999 atlassian/bitbucket-server

