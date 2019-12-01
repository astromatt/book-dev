*****
Extra
*****


Examples
========

Example 1
---------
.. code-block:: groovy
    :caption: Commit Hash from git shell

    // These should all be performed at the point where you've
    // checked out your sources on the agent. A 'git' executable
    // must be available.
    // Most typical, if you're not cloning into a sub directory
    shortCommit = sh(returnStdout: true, script: "git log -n 1 --pretty=format:'%h'").trim()

Example 2
---------
.. code-block:: groovy
    :caption: This shows a simple build wrapper example, using the AnsiColor plugin.

    node {

        // This displays colors using the 'xterm' ansi color map.
        ansiColor('xterm') {

            // Just some echoes to show the ANSI color.
            stage "\u001B[31mI'm Red\u001B[0m Now not"

        }
    }

Example 3
---------
.. code-block:: groovy
    :caption: Artifactory

     node {
        git url: 'https://github.com/jfrogdev/project-examples.git'

        // Get Artifactory server instance, defined in the Artifactory Plugin administration page.
        def server = Artifactory.server "SERVER_ID"

        // Read the upload spec and upload files to Artifactory.
        def downloadSpec =
                '''{
                "files": [
                    {
                        "pattern": "libs-snapshot-local/*.zip",
                        "target": "dependencies/",
                        "props": "p1=v1;p2=v2"
                    }
                ]
            }'''

        def buildInfo1 = server.download spec: downloadSpec

        // Read the upload spec which was downloaded from github.
        def uploadSpec =
                '''{
                "files": [
                    {
                        "pattern": "resources/Kermit.*",
                        "target": "libs-snapshot-local",
                        "props": "p1=v1;p2=v2"
                    },
                    {
                        "pattern": "resources/Frogger.*",
                        "target": "libs-snapshot-local"
                    }
                ]
            }'''

        // Upload to Artifactory.
        def buildInfo2 = server.upload spec: uploadSpec

        // Merge the upload and download build-info objects.
        buildInfo1.append buildInfo2

        // Publish the build to Artifactory
        server.publishBuildInfo buildInfo1
    }
