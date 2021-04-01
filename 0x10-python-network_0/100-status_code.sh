#!/bin/bash
# displays status code of response
curl -o /dev/null -s -w "%{http_code}" "$1"
