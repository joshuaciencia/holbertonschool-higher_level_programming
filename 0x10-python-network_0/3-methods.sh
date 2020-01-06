#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sI -X OPTIONS $1 | grep "Allow" | tail -1 | cut -d ':' -f2 | sed -e 's/^[[:space:]]*//'
