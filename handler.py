import json
from pptx import Presentation
import boto3
from time import gmtime, strftime

SLD_TITLE = 0
SLD_HEAD_COPY = 1
SLD_HEAD_SUBHEAD_COPY = 2
SLD_HEAD_ONLY = 7

def main(event, context):

  # dat = json.loads(event['body'])
  with open('9b.json') as f:
    dat = json.load(f)

  prs = Presentation('template_ki.pptx')

  title_layout = prs.slide_layouts[SLD_TITLE]
  # plain_layout = prs.slide_layouts[SLD_HEAD_COPY]

  subhead_txt = 'Rally ' + str(dat['rally_number']) + dat['sprint_letter']

  slide = prs.slides.add_slide(title_layout)
  slide.placeholders[0].text = dat['sprint_title']
  slide.placeholders[14].text = subhead_txt  # subhead
  slide.placeholders[15].text = dat['sprint_report'] # date
  slide.placeholders[17].text = 'Presented by ' + dat['presenter'] # speakers

  out = 'slides_' + strftime("%Y-%m-%d_%H%M%S", gmtime()) + '.pptx'

  prs.save('/tmp/' + out)

  s3 = boto3.resource("s3")
  s3.meta.client.upload_file('/tmp/' + out, 'ki-slides-bucket', out)
  object_acl = s3.ObjectAcl('ki-slides-bucket', out)
  response = object_acl.put(ACL='public-read')

  link = 'https://s3.amazonaws.com/ki-slides-bucket/' + out
  print(link)

  response = {
    "statusCode": 200,
    "body": link
  }

  return response

if __name__ == "__main__":
  main('', '')
