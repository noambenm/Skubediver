# Welcome to Skubediver!

Skubediver is an application designed to run in a Kubernetes cluster, providing scuba divers with essential tools to enhance their diving experience. This app aims to include the following features:

1. A simple dive log.
2. MOD (Maximum Operating Depth) and PO2 (Partial Pressure of Oxygen) calculators.
3. A database of popular dive sites worldwide.

### Development Progress (as of 13/11/24)

#### Completed Tasks

1. **Flask Backend**: Created a Flask backend with a POST endpoint to store the following fields in a MySQL database:
   - `dive_date`
   - `dive_time`
   - `max_depth`
   - `o2_percentage`
2. **Docker Image**: Built a Dockerfile for the dive log application and created an image.
3. **Kubernetes Configuration**: Set up Kubernetes deployment, services, ConfigMaps, and Secrets for both the dive log app and MySQL database.

#### Current Tasks in Progress

1. **Persistent Volume for MySQL Database**: Create a persistent storage solution to retain dive log data.
2. **Encryption in Secrets**: Implement encryption in Kubernetes secrets, using a type other than Opaque to enhance security.
3. **Basic Ingress Controller**: Configure a basic ingress controller using NGINX.
4. **Frontend for Dive Log Entry**: Develop a minimal frontend interface to input dive log data, simplifying the process without requiring tools like Postman.
