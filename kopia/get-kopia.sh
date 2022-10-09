#!/bin/bash
if [ -z $VERSION ]; then
  echo "Download latest"

  curl -s https://api.github.com/repos/kopia/kopia/releases/latest \
    | grep "browser_download_url.*linux-x64.tar.gz" \
    | cut -d : -f 2,3 \
    | tr -d \" \
    | xargs curl -#LO
else
  echo "Download $VERSION"

  curl -#LO https://github.com/kopia/kopia/releases/download/$VERSION/kopia-${VERSION:1}-linux-x64.tar.gz
fi

tar --one-top-level -xvf *linux-x64.tar.gz
mv */kopia kopia
