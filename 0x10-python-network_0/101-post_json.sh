#!/bin/bash
# displays if content type is valid json file or not
curl -sX POST -H "Content-Type: application/json" -d @$2 $1
