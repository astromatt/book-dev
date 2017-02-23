Rozwiązania
===========

Pull Requests builds
--------------------

Connect Jenkins with Stash:

- Install Stash Notifier Plugin in Jenkins
- In Configure System - Global Jenkins System Configuration set as follows

=============== ======================
Key             Value
=============== ======================
Stash Root URL  http://localhost:7990/
Stash User      ``jenkins``
Stash Password  ``jenkins``
=============== ======================


Pull Request Build Configuration
--------------------------------

Dashboard -> New Item -> "Freestyle project"

======================== ======================== =======================================================
Section                   Key                      Value
======================== ======================== =======================================================
                         Project name             `Pull Request`
Source Code Management   Source Code Management   `GIT`
Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
Source Code Management   Credentials              ``jenkins``
Source Code Management   [Advanced] -> Refspec    ``+refs/pull-requests/*/from:refs/remotes/origin/pr/*``
Source Code Management   Branch Specifier         ``**/pr/*``
Build Triggers           Schedule                 ``* * * * *``
Post-build Actions       Notify Stash Instance
======================== ======================== =======================================================


Master Branch Build Configuration
---------------------------------

Dashboard -> New Item -> "Freestyle project"

======================== ======================== =============================================
Section                  Key                      Value
======================== ======================== =============================================
                         Project name             `Master`
Source Code Management   Source Code Management   `GIT`
Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
Source Code Management   Credentials              ``jenkins``
Source Code Management   Branch Specifier         ``**/master``
Build Triggers           Schedule                 ``* * * * *``
Post-build Actions       Notify Stash Instance
======================== ======================== =============================================

Feature Branch Build Configuration
----------------------------------

Dashboard -> New Item -> "Freestyle project"

======================== ======================== =============================================
Section                  Key                      Value
======================== ======================== =============================================
                         Project name             `Feature`
Source Code Management   Source Code Management   `GIT`
Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
Source Code Management   Credentials              ``jenkins``
Source Code Management   Branch Specifier         ``*/feature/*``
Build Triggers           Schedule                 ``* * * * *``
Post-build Actions       Notify Stash Instance
======================== ======================== =============================================

Bugfix Branch Build Configuration
---------------------------------

Dashboard -> New Item -> "Freestyle project"

======================== ======================== =============================================
Section                  Key                      Value
======================== ======================== =============================================
                         Project name             `Feature`
Source Code Management   Source Code Management   `GIT`
Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
Source Code Management   Credentials              ``jenkins``
Source Code Management   Branch Specifier         ``*/bugfix/*``
Build Triggers           Schedule                 ``* * * * *``
Post-build Actions       Notify Stash Instance
======================== ======================== =============================================

Jenkins i testy wydajnościowe JMeter
------------------------------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <jmeterTestPlan version="1.2" properties="2.8" jmeter="2.13 r1665067">
      <hashTree>
        <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="Test Plan" enabled="true">
          <stringProp name="TestPlan.comments"></stringProp>
          <boolProp name="TestPlan.functional_mode">false</boolProp>
          <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>
          <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
          <stringProp name="TestPlan.user_define_classpath"></stringProp>
        </TestPlan>
        <hashTree>
          <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">
            <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
            <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
              <boolProp name="LoopController.continue_forever">false</boolProp>
              <stringProp name="LoopController.loops">1</stringProp>
            </elementProp>
            <stringProp name="ThreadGroup.num_threads">1</stringProp>
            <stringProp name="ThreadGroup.ramp_time">1</stringProp>
            <longProp name="ThreadGroup.start_time">1462974797000</longProp>
            <longProp name="ThreadGroup.end_time">1462974797000</longProp>
            <boolProp name="ThreadGroup.scheduler">false</boolProp>
            <stringProp name="ThreadGroup.duration"></stringProp>
            <stringProp name="ThreadGroup.delay"></stringProp>
          </ThreadGroup>
          <hashTree>
            <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP Request" enabled="true">
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
                <collectionProp name="Arguments.arguments"/>
              </elementProp>
              <stringProp name="HTTPSampler.domain">localhost</stringProp>
              <stringProp name="HTTPSampler.port">8080</stringProp>
              <stringProp name="HTTPSampler.connect_timeout"></stringProp>
              <stringProp name="HTTPSampler.response_timeout"></stringProp>
              <stringProp name="HTTPSampler.protocol"></stringProp>
              <stringProp name="HTTPSampler.contentEncoding"></stringProp>
              <stringProp name="HTTPSampler.path">/</stringProp>
              <stringProp name="HTTPSampler.method">GET</stringProp>
              <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
              <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
              <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
              <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
              <boolProp name="HTTPSampler.monitor">false</boolProp>
              <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
            </HTTPSamplerProxy>
            <hashTree/>
          </hashTree>
        </hashTree>
      </hashTree>
    </jmeterTestPlan>
