FROM amazoncorretto:17-alpine3.15

WORKDIR /app

ADD ./target/aline-gateway-*.jar aline-gateway.jar

ENV SERVICE_NAME="gateway"
RUN addgroup --gid 1001 -S $SERVICE_NAME && \
    adduser -G $SERVICE_NAME --shell /bin/false --disabled-password -H --uid 1001 $SERVICE_NAME

EXPOSE 8080

USER $SERVICE_NAME

ENTRYPOINT ["java", "-jar", "aline-gateway.jar"]
