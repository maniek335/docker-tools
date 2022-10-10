#!/bin/bash

if [ -z $VERSION ]; then
  echo "Download latest"

  curl -#LO https://github.com/containrrr/watchtower/releases/latest/download/watchtower_linux_amd64.tar.gz
else
  echo "Download $VERSION"

  curl -#LO https://github.com/containrrr/watchtower/releases/download/$VERSION/watchtower_linux_amd64.tar.gz
fi

tar --one-top-level -xvf watchtower_linux_amd64.tar.gz
mv */watchtower watchtower
