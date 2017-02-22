********
Findbugs
********

Install
=======

Add this to your ``pom.xml``

.. code-block:: xml

    <project>
        <reporting>
            <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>findbugs-maven-plugin</artifactId>
                <version>3.0.4-SNAPSHOT</version>
            </plugin>
            </plugins>
        </reporting>
    </project>

Usage
=====

.. code-block:: shell

    $ mvn site
