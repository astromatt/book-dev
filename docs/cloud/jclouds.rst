JClouds
=======
Apache jclouds® is an open source multi-cloud toolkit for the Java platform that gives you the freedom to create applications that are portable across clouds while giving you full control to use cloud-specific features.

Prividers
---------
- https://jclouds.apache.org/reference/providers/

Installation
------------
.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <properties>
        <jclouds.version>2.0.1</jclouds.version>
      </properties>
      <groupId>com.mycompany.app</groupId>
      <artifactId>my-app</artifactId>
      <version>1.0-SNAPSHOT</version>
      <dependencies>
        <dependency>
            <groupId>org.apache.jclouds</groupId>
            <artifactId>jclouds-all</artifactId>
            <version>${jclouds.version}</version>
          </dependency>
      </dependencies>
    </project>

Examples
--------
- https://github.com/jclouds/jclouds-examples
