# https://python-pptx.readthedocs.io/en/latest/user/presentations.html

SLD_TITLE = 0
SLD_HEAD_COPY = 1
SLD_HEAD_SUBHEAD_COPY = 2
SLD_HEAD_ONLY = 7

from pptx import Presentation

prs = Presentation('template_ki.pptx')

title_layout = prs.slide_layouts[SLD_TITLE]
plain_layout = prs.slide_layouts[SLD_HEAD_COPY]

slide = prs.slides.add_slide(title_layout)
for shape in slide.placeholders:
  print('%d %s' % (shape.placeholder_format.idx, shape.name))
# 0 Title 1
# 14 Text Placeholder 2
# 15 Text Placeholder 3
# 17 Text Placeholder 4
slide.placeholders[0].text = "Test Title"
slide.placeholders[14].text = "Test SubHead" # subhead
slide.placeholders[15].text = "Test Date" # date
slide.placeholders[17].text = "Test Speaker" # speakers

slide2 = prs.slides.add_slide(plain_layout)
for shape in slide2.placeholders:
  print('%d %s' % (shape.placeholder_format.idx, shape.name))
# 0 Title 2
# 16 Text Placeholder 1

slide2.placeholders[0].text = "Test Title"
body = slide2.placeholders[16]
body.has_text_frame
text_frame = body.text_frame
text_frame.clear()
text_frame.paragraphs[0]
p = text_frame.paragraphs[0]
run = p.add_run()
run.text = 'Bold Text:'
font = run.font
font.bold = True
# font.name = 'Calibri'
# font.size = Pt(18)
# font.color.theme_color = MSO_THEME_COLOR.ACCENT_1
# run.hyperlink.address = 'https://github.com/scanny/python-pptx'
p = text_frame.add_paragraph()
p.text = "Text"

prs.save('test.pptx')


