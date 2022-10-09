#!/bin/bash
if [ -z $Image_Version ]; then
  echo "::set-output name=image_name::hasura-cli:latest"
else
  echo "::set-output name=image_name::hasura-cli:$Image_Version"
fi
