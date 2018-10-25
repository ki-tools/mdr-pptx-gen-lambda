# mdr-pptx-gen-lambda

## Usage

Slides are generated through HTTP POST:

```sh
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "rally_number": 1,
    "rally_title": "Test Rally Title",
    "sprint_letter": "A",
    "sprint_title": "Test Sprint Title",
    "sprint_report": "2018-11-18",
    "presenter": "Test Presenter"
  }' \
  https://53zpbtf7g2.execute-api.us-east-1.amazonaws.com/dev/
```

This returns a URL that you can visit to download the generated slide deck.

## Setup

This has already been deployed to AWS Lambda, but if there is need for others to deploy, this is how to set up your environment to do so.

Prerequisites:
- Clone this repo
- Install [node](https://nodejs.org)
- Install [Docker](https://www.docker.com/products/docker-desktop)
- Install Serverless (`npm install -g serverless`)
- [Set up AWS credentials for Serverless](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

```sh
npm install

serverless deploy
```
