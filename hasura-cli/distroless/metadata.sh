#!/bin/bash
if [ -z $Image_Version ]; then
  echo "::set-output name=image_name::hasura-cli:distroless"
else
  echo "::set-output name=image_name::hasura-cli:$Image_Version-distroless"
fi
