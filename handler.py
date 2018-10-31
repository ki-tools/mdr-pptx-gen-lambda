import json
from pptx import Presentation
import boto3
from time import gmtime, strftime
from cognition_api import get_slide_data

SLD_TITLE = 0
SLD_HEAD_COPY = 1
SLD_HEAD_SUBHEAD_COPY = 2
SLD_HEAD_ONLY = 7

def main(event, context):

  dat = json.loads(event['body'])
  # with open('9b.json') as f:
  #   dat = json.load(f)

  if 'id' in dat.keys():
    d = get_slide_data(str(dat['id']))
  else:
    d = {
      'sprint_id': dat['sprint_id'],
      'end_date': dat['end_date'],
      'title': dat['title'],
      'participants': dat['participants'],
      'presenter': dat['presenter']
    }

  prs = Presentation('template_ki.pptx')

  title_layout = prs.slide_layouts[SLD_TITLE]
  # plain_layout = prs.slide_layouts[SLD_HEAD_COPY]

  # subhead_txt = 'Rally ' + str(dat['rally_number']) + dat['sprint_letter']

  slide = prs.slides.add_slide(title_layout)

  slide.placeholders[0].text = 'Rally ' + d['sprint_id'] + ': ' + d['title']
  slide.placeholders[15].text = 'Completed ' + d['end_date'] # date
  slide.placeholders[17].text = 'Presented by ' + d['presenter'] + ' on behalf of rally participants ' + d['participants']

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
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": true,
      "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
      "Content-Type": "application/json"
    }
  }

  return response

if __name__ == '__main__':
  main('', '')
