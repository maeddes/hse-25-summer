# Use an official OpenJDK 21 runtime as a parent image
FROM eclipse-temurin:21-jdk

# Set the working directory
WORKDIR /app

# Copy the application JAR to the container
COPY target/*.jar app.jar

# Expose the application port (adjust as needed)
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "/app/app.jar"]


