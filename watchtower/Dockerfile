FROM buildpack-deps:curl as deps
ARG VERSION

WORKDIR /tmp
COPY get-watchtower.sh /bin/get-watchtower.sh
RUN get-watchtower.sh


FROM debian:bullseye

WORKDIR /app
COPY --from=deps /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=deps /tmp/watchtower /bin/watchtower

COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
