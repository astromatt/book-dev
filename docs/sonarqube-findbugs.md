# Findbugs

## Install

Add this to your `pom.xml`

    <project>
    ...
    <reporting>
        <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>findbugs-maven-plugin</artifactId>
            <version>3.0.4-SNAPSHOT</version>
        </plugin>
        </plugins>
    </reporting>
    ...
    </project>

## Run

    mvn site

