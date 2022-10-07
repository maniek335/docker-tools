FROM buildpack-deps:curl as build

RUN curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | bash

FROM gcr.io/distroless/static

ENV HASURA_GRAPHQL_ENDPOINT=http://hasura:8080

COPY --from=build /usr/local/bin/hasura /bin/hasura

ENTRYPOINT [ "hasura", "--skip-update-check" ]
