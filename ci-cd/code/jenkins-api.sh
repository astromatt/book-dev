curl -X POST http://localhost:8080/job/JOB_NAME/build \
    --user USER:TOKEN \
    --data-urlencode json='{
        "parameter": [
            {"name":"id", "value":"123"},
            {"name":"verbosity", "value":"high"}
        ]}'