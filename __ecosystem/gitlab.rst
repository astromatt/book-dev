GitLab CI/CD
============


* https://docs.gitlab.com/ee/ci/yaml/README.html
* ``.gitlab-ci.yml``

.. code-block:: yaml

    stages:
      - build
      - test

    build-code-job:
      stage: build
      script:
        - echo "Check the ruby version, then build some Ruby project files:"
        - ruby -v
        - rake

    test-code-job1:
      stage: test
      script:
        - echo "If the files are built successfully, test some files with one command:"
        - rake test1

    test-code-job2:
      stage: test
      script:
        - echo "If the files are built successfully, test other files with a different command:"
        - rake test2

.. code-block:: yaml

    stages:
      - build
      - test
      - deploy

    job 0:
      stage: .pre
      script: make something useful before build stage

    job 1:
      stage: build
      script: make build dependencies

    job 2:
      stage: build
      script: make build artifacts

    job 3:
      stage: test
      script: make test

    job 4:
      stage: deploy
      script: make deploy

    job 5:
      stage: .post
      script: make something useful at the end of pipeline
