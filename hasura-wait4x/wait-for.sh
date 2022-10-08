#!/bin/bash
set -e

# Extract postgres adress from HASURA_GRAPHQL_DATABASE_URL environment variable 
tmp=${HASURA_GRAPHQL_DATABASE_URL#*@} # remove prefix ending in "@"
postgres=${tmp%/*} # remove suffix starting with "/"

wait4x tcp $postgres

exec docker-entrypoint.sh "$@"
