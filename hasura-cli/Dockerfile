FROM buildpack-deps:curl

ARG VERSION

ENV HASURA_GRAPHQL_ENDPOINT=http://hasura:8080

RUN groupadd --gid 1000 hasura && useradd --uid 1000 --gid hasura --shell /bin/bash --create-home hasura

RUN curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | VERSION=$VERSION bash

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD [ "hasura" ]
