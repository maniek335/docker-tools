FROM buildpack-deps:curl as deps

ARG VERSION
RUN curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | VERSION=$VERSION bash


FROM gcr.io/distroless/static as distroless

ENV HASURA_GRAPHQL_ENDPOINT=http://hasura:8080
COPY --from=deps /usr/local/bin/hasura /bin/hasura

ENTRYPOINT [ "hasura", "--skip-update-check" ]


FROM gcr.io/distroless/static:nonroot as distroless-nonroot

ENV HASURA_GRAPHQL_ENDPOINT=http://hasura:8080
COPY --from=deps /usr/local/bin/hasura /bin/hasura

ENTRYPOINT [ "hasura", "--skip-update-check" ]


FROM debian:bullseye

ENV HASURA_GRAPHQL_ENDPOINT=http://hasura:8080

RUN groupadd --gid 1000 hasura && useradd --uid 1000 --gid hasura --shell /bin/bash --create-home hasura

COPY --from=deps /usr/local/bin/hasura /usr/local/bin/hasura

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
