#!/bin/bash

# before start - from the main dir run:
# docker build -t allrank:latest .

DIR=$(dirname $0)
PROJECT_DIR="$(cd $DIR/..; pwd)"

#docker run -e PYTHONPATH=/allrank -v $PROJECT_DIR:/allrank allrank:latest /bin/sh -c 'python allrank/data/generate_dummy_data.py && python allrank/main.py --config-file-name /allrank/scripts/local_config.json --run-id test_run --job-dir /allrank/task-data'
#docker run -e PYTHONPATH=/allrank -v $PROJECT_DIR:/allrank allrank:latest /bin/sh -c 'python allrank/main.py --config-file-name /allrank/config.json --run-id test_v1 --job-dir /allrank/task_v1'
#docker run --shm-size=4g -e PYTHONPATH=/allrank -v $PROJECT_DIR:/allrank allrank:latest /bin/sh -c 'python allrank/main.py --config-file-name /allrank/config2_lambdarank.json --run-id test_v2 --job-dir /allrank/task_v2'
docker run --shm-size=4g -e PYTHONPATH=/allrank -v $PROJECT_DIR:/allrank allrank:latest /bin/sh -c 'python allrank/main.py --config-file-name /allrank/config3_approxndcg.json --run-id test_v3 --job-dir /allrank/task_v3'


# python allrank/main.py --config-file-name config2_lambdarank_v3b.json --run-id test_v3 --job-dir task_v3