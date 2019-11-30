************
Post Actions
************


At the end of pipeline directive:

:``always``: Run the steps in the post section regardless of the completion status of the Pipeline’s or stage’s run.

:``changed``: Only run the steps in post if the current Pipeline’s or stage’s run has a different completion status from its previous run.

:``failure``: Only run the steps in post if the current Pipeline’s or stage’s run has a "failed" status, typically denoted by red in the web UI.

:``success``: Only run the steps in post if the current Pipeline’s or stage’s run has a "success" status, typically denoted by blue or green in the web UI.

:``unstable``: Only run the steps in post if the current Pipeline’s or stage’s run has an "unstable" status, usually caused by test failures, code violations, etc. This is typically denoted by yellow in the web UI.

:``aborted``: Only run the steps in post if the current Pipeline’s or stage’s run has an "aborted" status, usually due to the Pipeline being manually aborted. This is typically denoted by gray in the web UI

.. literalinclude:: code/jenkinsfile-post.groovy
    :language: groovy
    :caption: Post
