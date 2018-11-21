import json
from pptx import Presentation
import boto3
from time import gmtime, strftime
import requests
import os.path
from cognition_api import get_slide_data
from slides import make_slides

def main(event, context):

  dat = json.loads(event['body'])
  # with open('9b.json') as f:
  #   dat = json.load(f)

  if 'id' in dat.keys():
    d = get_slide_data(str(dat['id']))
  else:
    d = dat

  pptx_path = 'template_ki_empty.pptx'
  # if the slides URL is valid and we can download
  # then we will use this slide deck, otherwise fall
  # back on empty template
  if d['ds_slides_url'] != '':
    url = d['ds_slides_url']
    r = requests.get(url)
    with open('/tmp/pres.pptx', 'wb') as f:  
      f.write(r.content)
    if r.status_code == 200 and os.path.isfile('/tmp/pres.pptx'):
      pptx_path = '/tmp/pres.pptx'

  prs = Presentation(pptx_path)
  prs = make_slides(prs, d)

  out = 'rally' + d['sprint_id'] + '_' + strftime('%Y-%m-%d_%H%M%S', gmtime()) + '.pptx'

  prs.save('/tmp/' + out)

  s3 = boto3.resource('s3')
  s3.meta.client.upload_file('/tmp/' + out, 'ki-slides-bucket', out)
  object_acl = s3.ObjectAcl('ki-slides-bucket', out)
  response = object_acl.put(ACL = 'public-read')

  link = 'https://s3.amazonaws.com/ki-slides-bucket/' + out
  # print(link)

  response = {
    'statusCode': 200,
    'body': json.dumps({
      'url': link
    }),
    'headers': {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    }
  }

  return response

if __name__ == '__main__':
  main('', '')
