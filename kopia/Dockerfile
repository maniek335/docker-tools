FROM buildpack-deps:curl as deps
ARG VERSION

COPY get-kopia.sh /bin/get-kopia.sh

WORKDIR /tmp
RUN get-kopia.sh


FROM gcr.io/distroless/static as distroless

ENV KOPIA_CONFIG_PATH=/app/config/repository.config \
    KOPIA_LOG_DIR=/app/logs \
    KOPIA_CACHE_DIRECTORY=/app/cache \
    RCLONE_CONFIG=/app/rclone/rclone.conf \
    KOPIA_PERSIST_CREDENTIALS_ON_CONNECT=false \
    KOPIA_CHECK_FOR_UPDATES=false

WORKDIR /app
COPY --from=deps /tmp/kopia /bin/kopia

ENTRYPOINT ["/bin/kopia"]


FROM gcr.io/distroless/static:nonroot as distroless-nonroot

ENV KOPIA_CONFIG_PATH=/app/config/repository.config \
    KOPIA_LOG_DIR=/app/logs \
    KOPIA_CACHE_DIRECTORY=/app/cache \
    RCLONE_CONFIG=/app/rclone/rclone.conf \
    KOPIA_PERSIST_CREDENTIALS_ON_CONNECT=false \
    KOPIA_CHECK_FOR_UPDATES=false

WORKDIR /app
COPY --from=deps /tmp/kopia /bin/kopia

ENTRYPOINT ["/bin/kopia"]


FROM debian:bullseye

ENV KOPIA_CONFIG_PATH=/app/config/repository.config \
    KOPIA_LOG_DIR=/app/logs \
    KOPIA_CACHE_DIRECTORY=/app/cache \
    RCLONE_CONFIG=/app/rclone/rclone.conf \
    KOPIA_PERSIST_CREDENTIALS_ON_CONNECT=false \
    KOPIA_CHECK_FOR_UPDATES=false
  
RUN groupadd --gid 1000 kopia && useradd --uid 1000 --gid kopia --shell /bin/bash --create-home kopia

WORKDIR /app
COPY --from=deps /tmp/kopia /bin/kopia

ENTRYPOINT ["/bin/kopia"]
