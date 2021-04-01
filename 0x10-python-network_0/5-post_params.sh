#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=test@test_mail.com&subject=hello world!" "$1"
