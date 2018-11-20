# https://python-pptx.readthedocs.io/en/latest/user/presentations.html

SLD_TITLE = 0
SLD_HEAD_COPY = 1
SLD_HEAD_SUBHEAD_COPY = 2
SLD_HEAD_ONLY = 7

from pptx import Presentation
from cognition_api import get_slide_data

# title slide
# background
# questions
# motivation
# deliverables?
# data/methods/results (insert)
# value
# next steps

d = get_slide_data('135')

# prs = Presentation('template_ki.pptx')
prs = Presentation('template_results_ki.pptx')

# id_dict = { slide.id: [i, slide.rId] for i,slide in enumerate(prs.slides._sldIdLst) }
# len(prs.slides)

# make title slide
title_layout = prs.slide_layouts[SLD_TITLE]
plain_layout = prs.slide_layouts[SLD_HEAD_COPY]

slide = prs.slides.add_slide(title_layout)
for shape in slide.placeholders:
  print('%d %s' % (shape.placeholder_format.idx, shape.name))
# 0 Title 1
# 15 Text Placeholder 3
# 17 Text Placeholder 4
slide.placeholders[0].text = 'Rally ' + d['sprint_id'] + ': ' + d['title']
slide.placeholders[15].text = 'Completed ' + d['end_date'] # date
slide.placeholders[17].text = 'Presented by ' + d['presenter'] + ' on behalf of rally participants ' + d['participants']

# slide2 = prs.slides.add_slide(plain_layout)
# for shape in slide2.placeholders:
#   print('%d %s' % (shape.placeholder_format.idx, shape.name))
# # 0 Title 2
# # 16 Text Placeholder 1

# slide2.placeholders[0].text = "Test Title"
# body = slide2.placeholders[16]
# body.has_text_frame
# text_frame = body.text_frame
# text_frame.clear()
# text_frame.paragraphs[0]
# p = text_frame.paragraphs[0]
# run = p.add_run()
# run.text = 'Bold Text:'
# font = run.font
# font.bold = True
# # font.name = 'Calibri'
# # font.size = Pt(18)
# # font.color.theme_color = MSO_THEME_COLOR.ACCENT_1
# # run.hyperlink.address = 'https://github.com/scanny/python-pptx'
# p = text_frame.add_paragraph()
# p.text = "Text"

# move title slide to slide 1
last_slide = len(prs.slides) - 1
slides = list(prs.slides._sldIdLst)
prs.slides._sldIdLst.remove(slides[last_slide])
prs.slides._sldIdLst.insert(0, slides[last_slide])

# remove INSTRUCTIONS slide before saving
slides = list(prs.slides)
slides2 = list(prs.slides._sldIdLst)
rm_idx = next((i for i in range(len(slides)) if slides[i].slide_layout.name == 'INSTRUCTIONS'), None)
if rm_idx != None:
  prs.slides._sldIdLst.remove(slides2[rm_idx])

prs.save('test.pptx')
