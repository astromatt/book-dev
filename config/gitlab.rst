GitLab
======

* ``.gitlab-ci.yml``

.. code-block:: yaml

    # Refs to skip
    skip_refs: “deploy*”

    # Run before each script

    # Refs to skip
    skip_refs: “deploy*”

    # Run before each script
    before_script:
      - export PATH=$HOME/bin:/usr/local/bin:/usr/bin:/bin
      - gem install bundler
      - cp config/database.yml.mysql config/database.yml
      - cp config/gitlab.yml.example config/gitlab.yml
      - touch log/application.log
      - touch log/test.log
      - bundle install --without postgres production --jobs $(nproc)
      - “bundle exec rake db:create RAILS_ENV=test”

    # Parallel jobs, each line is a parallel build
    jobs:
      - script: “rake spec”
        runner: “ruby,postgres”
        name: “Rspec”
      - script: “rake spinach”
        runner: “ruby,mysql”
        name: “Spinach”
        tags: true
        branches: false

    # Parallel deploy jobs
    on_success:
      - “cap deploy production”
      - “cap deploy staging”

.. code-block:: yaml

    before_script:
      - gem install bundler
      - bundle install
      - bundle exec rake db:create

    rspec:
      test: "rake spec"
      tags:
        - ruby
        - postgres
      only:
        - branches

    spinach:
      test: "rake spinach"
      tags:
        - ruby
        - mysql
      except:
        - tags

    staging:
      deploy: "cap deploy stating"
      tags:
        - capistrano
        - debian
      except:
        - stable

    production:
      deploy:
        - cap deploy production
        - cap notify
      tags:
        - capistrano
        - debian
      only:
        - master
        - /^deploy-.*$/
