# Docker Project: DevOps Technical Scenario for an E-commerce Web Application

This Docker project is designed to provide an environment with multiple services to help developers easily build and test applications that require Python, Node.js, PHP, MySQL, MongoDB, and Redis. This project uses Docker Compose to manage the various containers and services.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/silviafpp/docker_work.git
```
2. Navigate to the root directory of the project in your terminal.

3. Run the following command to start the containers:

```bash
docker compose up -d
```
## Services
The following services are included in this setup:

    Python
    Node.js
    PHP
    MySQL
    MongoDB
    Redis
    
## Usage

Once the services are up and running, you can access the various services using their respective ports:

- Node.js: localhost:3000
- PHP: localhost:8000
- Python: localhost:5000
- Adminer: localhost:8080

### You can access the MySQL database using the following credentials:

- Server: db
- Username: root
- Password: example
- Database: user

### You can access the MongoDB database using the following command in terminal:

```
docker exec -it mongodb mongo
```

### You can access the Redis database using the following command in the terminal:

```
docker exec -it redis redis-cli
```


