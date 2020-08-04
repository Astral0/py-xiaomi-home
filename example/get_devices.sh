#!/bin/bash

set_root() {
    local this=`readlink -n -f $1`
    root=`dirname $this`
}
set_root $0

# if [ -f "${root}/../../config/devices.json" ]; then
    # cat ${root}/../../config/devices.json
# fi

export PYTHONPATH=${root}/..
cd ${root}/
python2 ${root}/get_gateways.py
