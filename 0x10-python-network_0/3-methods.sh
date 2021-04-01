#!/bin/bash
#
curl -sI "$1" | grep Allow | cut -c 8-
