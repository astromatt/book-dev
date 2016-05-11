# Puppet Tomcat installation and configuration

```puppet
class { 'java': }

tomcat::install { '/opt/tomcat8':
  source_url => 'https://www.apache.org/dist/tomcat/tomcat-8/v8.0.33/bin/apache-tomcat-8.0.33.tar.gz'
}

tomcat::instance { 'tomcat8-first':
  catalina_home => '/opt/tomcat8',
  catalina_base => '/opt/tomcat8/first',
}

tomcat::instance { 'tomcat8-second':
  catalina_home => '/opt/tomcat8',
  catalina_base => '/opt/tomcat8/second',
}

# Change the default port of the second instance server and HTTP connector
tomcat::config::server { 'tomcat8-second':
  catalina_base => '/opt/tomcat8/second',
  port          => '8006',
}

tomcat::config::server::connector { 'tomcat8-second-http':
  catalina_base         => '/opt/tomcat8/second',
  port                  => '8081',
  protocol              => 'HTTP/1.1',
  additional_attributes => {
    'redirectPort' => '8443'
  },
}

tomcat::war { 'sample.war':
  catalina_base => '/opt/tomcat8/first',
  war_source    => '/opt/tomcat8/webapps/docs/appdev/sample/sample.war',
}
```
