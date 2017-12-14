JIRA_HOME="/opt/jira/home"
JVM_SUPPORT_RECOMMENDED_ARGS="-server -XX:MaxPermSize=512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+PrintGC -XX:+PrintGCDateStamps -XX:+OptimizeStringConcat -XX:+PrintGCDetails -XX:+DisableExplicitGC -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%Y.%m.%d).log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M"
JVM_MINIMUM_MEMORY="512m"
JVM_MAXIMUM_MEMORY="2048m"

# -server
# -XX:MaxPermSize=512m
# -XX:+UseG1GC
# -XX:+PrintGC
# -XX:MaxGCPauseMillis=200
# -XX:+PrintGCDateStamps
# -XX:+PrintGCDetails
# -XX:+UseGCLogFileRotation
# -XX:GCLogFileSize=10M
# -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%F).log
# -XX:NumberOfGCLogFiles=10
# -XX:+OptimizeStringConcat
# -XX:+DisableExplicitGC



# -Xms --> Minimum Memory
# -Xmx --> Maximum Memory
# -Xmn --> Heap of Younger Generation
# -Xss --> Thread Stack Size
# -XX:MaxMetaspaceSize --> Maximum Memory for Non-Heap Metaspace.
# -XX:NewRatio --> Ratio between Younger and Older Generation Memory sizes.
# -XX:ParallelGCThreads --> No of Parallel GC threads. By default, the GC threads will be equal to the number of CPUs of the Node / VM. Used when Parallel Garbage collectors are configured.






GC_JVM_PARAMETERS=""
GC_JVM_PARAMETERS="-XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+PrintGCCause ${GC_JVM_PARAMETERS}"
GC_JVM_PARAMETERS="-Xloggc:$LOGBASEABS/logs/atlassian-jira-gc-%t.log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSize=20M ${GC_JVM_PARAMETERS}"




## Defaultowe ustawienia Jiry po instalacji:
/opt/atlassian/jira/jre//bin/java
	-Djava.util.logging.config.file=/opt/atlassian/jira/conf/logging.properties
	-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
	-Xms384m
	-Xmx768m
	-Djava.awt.headless=true
	-Datlassian.standalone=JIRA
	-Dorg.apache.jasper.runtime.BodyContentImpl.LIMIT_BUFFER=true
	-Dmail.mime.decodeparameters=true
	-Dorg.dom4j.factory=com.atlassian.core.xml.InterningDocumentFactory
	-XX:-OmitStackTraceInFastThrow
	-Datlassian.plugins.startup.options=
	-Djdk.tls.ephemeralDHKeySize=2048
	-Djava.protocol.handler.pkgs=org.apache.catalina.webresources
	-Xloggc:/opt/atlassian/jira/logs/atlassian-jira-gc-%t.log
	-XX:+UseGCLogFileRotation
	-XX:NumberOfGCLogFiles=5
	-XX:GCLogFileSize=20M
	-XX:+PrintGCDetails
	-XX:+PrintGCDateStamps
	-XX:+PrintGCTimeStamps
	-XX:+PrintGCCause
	-classpath /opt/atlassian/jira/bin/bootstrap.jar:/opt/atlassian/jira/bin/tomcat-juli.jar
	-Dcatalina.base=/opt/atlassian/jira
	-Dcatalina.home=/opt/atlassian/jira
	-Djava.io.tmpdir=/opt/atlassian/jira/temp
	org.apache.catalina.startup.Bootstrap start