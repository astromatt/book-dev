JIRA_HOME="/opt/jira/home"
JVM_SUPPORT_RECOMMENDED_ARGS="-server -XX:MaxPermSize=512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+PrintGC -XX:+PrintGCDateStamps -XX:+OptimizeStringConcat -XX:+PrintGCDetails -XX:+DisableExplicitGC -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%Y.%m.%d).log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M"
JVM_MINIMUM_MEMORY="512m"
JVM_MAXIMUM_MEMORY="2048m"


# -Xms --> Minimum Memory
# -Xmx --> Maximum Memory
# -Xmn --> Heap of Younger Generation
# -Xss --> Thread Stack Size
# -XX:MaxMetaspaceSize --> Maximum Memory for Non-Heap Metaspace.
# -XX:NewRatio --> Ratio between Younger and Older Generation Memory sizes.
# -XX:ParallelGCThreads --> No of Parallel GC threads. By default, the GC threads will be equal to the number of CPUs of the Node / VM. Used when Parallel Garbage collectors are configured.