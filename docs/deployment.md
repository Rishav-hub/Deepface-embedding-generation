# Manually Deploy Application to Google Cloud Platform (GCP)

This document describes how to manually deploy the application to Google Cloud Platform (GCP).

## Prerequisites
1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts).
2. Install [Docker](https://docs.docker.com/get-docker/).
3. You must have ONE of the following:
    - Owner
    - Editor
    - Both the Cloud Run Admin and Service Account User roles
4. You must have a GCP project with billing enabled. If you don't have a project, you can create one from the [GCP Console](https://console.cloud.google.com/projectcreate).

## Steps
1. Push the docker image that you must have build in your local to Google Artifact Registry.
    ```bash
    docker tag <your-image-name> gcr.io/<your-project-id>/<your-image-name>
    docker push gcr.io/<your-project-id>/<your-image-name>
    ```
2. Go to Google Cloud Run and create a new service.
3. Select the region you want to deploy to.
4. Select the docker image you just pushed to Google Artifact Registry.
5. Set the port which would be needed to be exposed.
6. Click on "Deploy".
3. You can access the application at the URL that is displayed in the output of the previous command.