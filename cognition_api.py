import requests
import json

def get_slide_data(id):

  resp = requests.get('http://api.cognitionstudio.com/api/v1/analysis/' + str(id))
  if resp.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

  a = resp.json()['data']
  return process_slide_data(a)

def process_slide_data(a):
  MISSING = '[MISSING IN RALLY WEB FORM]'

  prt = a['participants']
  if not isinstance(prt, list):
    prt = ['']
  if prt == ['']:
    participant_list = [{ 'first_name': MISSING, 'last_name': ''}]
  else:
    participant_ids = list(map(int, a['participants']))
    participant_list = list(filter(lambda item: item['id'] in participant_ids, a['users']))
  participants = ', '.join(
    list(map(lambda x: x['first_name'] + ' ' + x['last_name'], participant_list)))

  title = str(a['sprint_title'] or MISSING)

  timeline = a['timeline']
  if not isinstance(timeline, list):
    timeline = ['']
  if (len(timeline) != 2):
    end_date = MISSING
  else:
    end_date = timeline[1]

  sprint_id = a['rally_number'] + a['sprint_letter'].upper()

  presenter_id = int(a['presenter'] or -1)
  if presenter_id == -1:
    presenter = MISSING
  else:
    presenter_list = list(filter(lambda item: item['id'] == presenter_id, a['users']))
    if len(presenter_list) == 0:
      presenter = '[NOT FOUND IN USER LIST]'
    else:
      presenter = presenter_list[0]

  key_findings = a['key_findings']
  if not isinstance(key_findings, list):
    key_findings = [MISSING]
  if len(key_findings) == 0:
    key_findings = [MISSING]

  value = a['value']
  if not isinstance(value, str):
    value = MISSING
  if value == '':
    value = MISSING

  next_steps = a['next_steps']
  if not isinstance(next_steps, list):
    next_steps = [MISSING]
  if len(next_steps) == 0:
    next_steps = [MISSING]

  deliverables = a['deliverables']
  if not isinstance(deliverables, list):
    deliverables = [MISSING]
  if len(deliverables) == 0:
    deliverables = [MISSING]

  motivation = a['motivation']
  if not isinstance(motivation, str):
    motivation = MISSING
  if motivation == '':
    motivation = MISSING

  background = a['background']
  if not isinstance(background, str):
    background = MISSING
  if background == '':
    background = MISSING

  problem_statement = a['problem_statement']
  if not isinstance(problem_statement, str):
    problem_statement = MISSING
  if problem_statement == '':
    problem_statement = MISSING

  sprint_question = a['sprint_question']
  if not isinstance(sprint_question, list):
    sprint_question = [MISSING]
  if len(sprint_question) == 0:
    sprint_question = [MISSING]

  return {
    'sprint_id': sprint_id,
    'end_date': end_date,
    'title': title,
    'participants': participants,
    'presenter': presenter,
    'key_findings': key_findings,
    'value': value,
    'next_steps': next_steps,
    'deliverables': deliverables,
    'motivation': motivation,
    'background': background,
    'problem_statement': problem_statement,
    'sprint_question': sprint_question,
    'ds_slides_url': ''
  }


# a['methods_all']
# a['prioritized_questions']
# a['tags_all']
# a['variables']
# a['users']


# a['sprint_question']
# a['deliverables']
# a['key_findings']
# a['tags']
# a['background_detail']
# a['final_impact_value']
# a['sprint_title']
# a['prioritized_question']
# a['participants']
# a['analysis_plan']
# a['created_date']
# a['revisions']
# a['background']
# a['previous_sprint']
# a['timeline']
# a['dataset_list']

# # a['methods']
# a['id']
# a['rally_title']
# a['updated_date']
# a['presenter']
# a['problem_statement']
# # a['method_details']
# a['sprint_focus']
# a['user']
# a['motivation']
# # a['status']
# a['next_steps']
# # a['data_description']


# # a.keys()

# a['deliverables']
# a['problem_statement']
# a['sprint_title']
# a['sprint_letter']

# a['key_findings']
# a['users']
