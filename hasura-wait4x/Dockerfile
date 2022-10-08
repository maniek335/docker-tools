ARG VERSION

FROM buildpack-deps:curl as build

WORKDIR /tmp

RUN curl -#LO https://github.com/atkrad/wait4x/releases/latest/download/wait4x-linux-amd64.tar.gz; \
    tar --one-top-level -xvf wait4x-linux-amd64.tar.gz


FROM hasura/graphql-engine:${VERSION}.cli-migrations-v3

COPY --from=build /tmp/wait4x-linux-amd64/wait4x /bin/wait4x

COPY /wait-for.sh /bin/wait-for.sh
ENTRYPOINT [ "wait-for.sh" ]

CMD $HGE_BINARY serve
