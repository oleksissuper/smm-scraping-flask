# 1. Installation

git clone <repository-url>
cd <project-directory>

# 2. Environment Setup

## .env File

To configure the project, you need to create a `.env` file in the root directory of the project. This file should contain the following environment variables:

### Database Connection (MySQL)

Provide the details to connect to your MySQL database:

DB_HOST=db
DB_PORT=3306
DB_DATABASE=
DB_USER=
DB_PASSWORD=
MYSQL_ROOT_PASSWORD=

### Logging Configuration

LOGS_LEVEL=DEBUG
LOGS_DIR=logs
LOGS_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s
LOGS_ROLLOVER=true

### API Keys

POSTLIKES_API_KEY=
BULKFOLLOWS_API_KEY=
FOLLOWIZ_API_KEY=

# 3. Install Docker Compose on Server

## Step 1: Update the package manager

sudo apt-get update

## Step 2: Install Docker (if not already installed)

sudo apt-get install docker.io -y

## Step 3: Verify Docker Compose availability

docker compose version

## Step 4: Enable Docker service

sudo systemctl start docker
sudo systemctl enable docker

# 4. Run Docker Compose (This way, three Docker containers will be launched: MySQL database, scraper, and Flask API.)

docker compose build --no-cache && docker compose up -d

### Essential Docker Commands (I think you need only these commands.)

#### 1. docker ps

- **Description**: Displays a list of all running containers.

#### 2. docker compose restart

- **Description**: Restarts all or specific services defined in the docker-compose.yml file.

#### 3. docker logs <container_id_or_name>

- **Description**: Displays the logs of a specific container. (docker ps - show containers)
