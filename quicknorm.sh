#!/bin/bash

REPO="https://github.com/jotuel/norminetteplus.git"

TARGET_DIR="/Users/$USER/goinfre/quicknorm_temp_"

# because we are using a potentially dangerous rm -rf, we randomize 16
# chars in the directory name which we use and remove.
RAND_STR=$(cat /dev/urandom | LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1)

TARGET_DIR+=$RAND_STR

git clone -q $REPO $TARGET_DIR && python3 $TARGET_DIR/run.py; rm -rf $TARGET_DIR
