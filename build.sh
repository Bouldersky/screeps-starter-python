#!/bin/bash

docker run --rm \
    --network="host"\
    --name "screeps-builder"\
    --mount type=bind,source="`pwd`/src",target=/root/src\
    --mount type=bind,source="`pwd`/config.json",target=/root/config.json\
    screeps-env:latest\
    /root/build.py
    #/bin/sh -i
