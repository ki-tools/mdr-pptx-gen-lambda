# mdr-pptx-gen-lambda

## Usage

Slides are generated through HTTP POST.

Directly with data:

```sh
curl \
  --request POST \
  --data '{
    "sprint_id": "1A",
    "end_date": "2018-11-18",
    "title": "Test Sprint Title",
    "participants": "Participant 1, Participant 2",
    "presenter": "Test Presenter"
  }' \
  https://vmvuauvf2a.execute-api.us-east-1.amazonaws.com/dev/
```

With a rally ID which is used to pull data from the api:

```sh
curl -v \
  --request POST \
  --data '{ "id": 156 }' \
  https://vmvuauvf2a.execute-api.us-east-1.amazonaws.com/dev/
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
