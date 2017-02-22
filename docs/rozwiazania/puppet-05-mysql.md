# Puppet MySQL installation and configuration

```puppet
class { "mysql::server":
    root_password => "mypassword",
    #remove_default_accounts => true,
    override_options => {
        mysqld => {
            "bind_address"  => "0.0.0.0",
        }
    },
    databases => {
      'mydb' => {
        ensure  => 'present',
        charset => 'utf8',
      },
    },
    users => {
      'myusername@%' => {
        ensure          => 'present',
        password_hash   => mysql_password("mypassword"),
      },
    },
    grants => {
      'myusername@%/mydb.*' => {
        ensure      => 'present',
        privileges  => ["all"],
        table       => "mydb.*",
        user        => "myusername@%",
      },
    },
}

# Enable MySQL Backups
class { "mysql::server::backup":
    backupuser      => "myusername",
    backuppassword  => "mypassword",
    backupdir       => "/tmp/mysql_backup",
}
```
