FROM openjdk:17
ADD aline-gateway-0.1.0.jar aline-gateway-0.1.0.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "aline-gateway-0.1.0.jar"]
