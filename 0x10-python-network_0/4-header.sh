#!/bin/bash
# displays the body of the response to header variable X-Python-User-Id
curl -sH "X-Python-User-Id: 98" "$1"
