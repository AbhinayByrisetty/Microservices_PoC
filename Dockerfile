FROM datawire/ambassador-envoy:latest

ENV http_proxy http://138.85.224.137:8080

# This Dockerfile is set up to install all the application-specific stuff into
# /application.

# We need curl, pip, and dnsutils (for nslookup).
RUN apt-get update && apt-get -q install -y \
    curl \
    dnsutils

ENTRYPOINT [ "/usr/local/bin/envoy" ]
CMD [ "-c", "/etc/envoy/envoy.json" ]
