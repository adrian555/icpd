FROM python:3 as manifests

RUN pip3 install operator-courier==1.0.2
COPY operators operators
RUN for file in ./operators/*; do operator-courier nest $file /manifests/$(basename $file); done

FROM docker.io/ffdlops/upstream-registry-builder:v1.1.0 as builder
COPY --from=manifests /manifests manifests
RUN ./bin/initializer -o ./bundles.db

FROM scratch
COPY --from=builder /build/bundles.db /bundles.db
COPY --from=builder /build/bin/registry-server /registry-server
COPY --from=builder /bin/grpc_health_probe /bin/grpc_health_probe
EXPOSE 50051
ENTRYPOINT ["/registry-server"]
CMD ["--database", "bundles.db"]

