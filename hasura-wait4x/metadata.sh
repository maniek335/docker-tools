#!/bin/bash
if [ -z $Image_Version ]; then
  echo "::set-output name=image_name::hasura-wait4x:latest"
else
  echo "::set-output name=image_name::hasura-wait4x:$Image_Version"
fi
