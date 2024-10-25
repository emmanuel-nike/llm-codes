import docker
import os
import sys

# Configuration parameters
IMAGE_NAME = "python:3.9-slim"
CONTAINER_NAME = "web_app_container"
DOCKERFILE_PATH = "./Dockerfile"
HOST_PORT = 8081  # Port on the host
CONTAINER_PORT = 5000  # Port in the container

def build_docker_image(client):
    """Build the Docker image from Dockerfile."""
    try:
        print("Building Docker image...")
        image, build_logs = client.images.build(path=".", tag=IMAGE_NAME)
        
        # Display build logs
        for line in build_logs:
            if 'stream' in line:
                print(line['stream'].strip())
                
        print(f"Docker image '{IMAGE_NAME}' built successfully.")
        return image
    except docker.errors.BuildError as err:
        print("Error during Docker image build:", err)
        sys.exit(1)

def run_docker_container(client):
    """Run the Docker container."""
    try:
        print("Running Docker container...")
        # Stop and remove the existing container if it's running
        try:
            container = client.containers.get(CONTAINER_NAME)
            print(f"Stopping and removing existing container '{CONTAINER_NAME}'...")
            container.stop()
            container.remove()
        except docker.errors.NotFound:
            pass  # No container to remove

        # Run a new container with specified ports and name
        container = client.containers.run(
            IMAGE_NAME,
            name=CONTAINER_NAME,
            ports={f"{CONTAINER_PORT}/tcp": HOST_PORT},
            detach=True  # Run container in the background
        )
        
        print(f"Container '{CONTAINER_NAME}' is running on port {HOST_PORT}.")
        return container
    except docker.errors.ContainerError as err:
        print("Error during Docker container run:", err)
        sys.exit(1)

def main():
    # Ensure Dockerfile exists
    if not os.path.exists(DOCKERFILE_PATH):
        print(f"Dockerfile not found at '{DOCKERFILE_PATH}'.")
        sys.exit(1)

    # Initialize Docker client
    client = docker.from_env()

    # Build Docker image
    build_docker_image(client)

    # Run Docker container
    run_docker_container(client)

if __name__ == "__main__":
    main()
