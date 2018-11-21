# mdr-pptx-gen-lambda

## Usage

Slides are generated through HTTP POST.

Directly with data:

```sh
curl \
  --request POST \
  --data '{
    "title": "Sprint Title",
    "presenter": "First Last",
    "sprint_id": "1A",
    "participants": "First Last, First Last, First Last, First Last",
    "end_date": "2018-01-01",
    "sprint_question": [
      "Question 1",
      "Question 2",
      "Question 3"
    ],
    "background": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pulvinar nibh sed mauris convallis dapibus. Nunc venenatis tempus nulla sit amet viverra.",
    "problem_statement": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pulvinar nibh sed mauris convallis dapibus. Nunc venenatis tempus nulla sit amet viverra.",
    "motivation": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pulvinar nibh sed mauris convallis dapibus. Nunc venenatis tempus nulla sit amet viverra.",
    "deliverables": [
      "Deliverable 1",
      "Deliverable 2",
      "Deliverable 3"
    ],
    "key_findings": [
      "Finding 1",
      "Finding 2",
      "Finding 3"
    ],
    "next_steps": [
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pulvinar nibh sed mauris convallis dapibus. Nunc venenatis tempus nulla sit amet viverra.",
    "ds_slides_url": ""
  }' \
  https://vmvuauvf2a.execute-api.us-east-1.amazonaws.com/dev/
```

With a rally ID which is used to pull data from the api:

```sh
curl -v \
  --request POST \
  --data '{ "id": 120 }' \
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
