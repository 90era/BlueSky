#!/bin/sh
dir=$(cd $(dirname $0); pwd)
tail -f ${dir}/logs/sys.log | grep -n --color=auto $(date +%F)