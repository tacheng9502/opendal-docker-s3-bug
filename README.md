# OpenDAL Docker Bug Reproduction

This repository reproduces an issue with OpenDAL's Python binding when performing operations on an S3 bucket in a Docker environment.

## Steps to Reproduce

1. Clone the repository:
   ```bash
   git clone https://github.com/tacheng9502/opendal-docker-s3-bug.git
   cd opendal-docker-bug
   ```
2. Update the .env file with your S3 credentials:
   ```bash
   cp example.env .env
   # Edit .env with your credentials
   ```
3. Build and run the Docker container:
   ```bash
   docker build -t opendal-docker-bug .
   docker run --env-file .env opendal-docker-bug
   ```
