from jinja2 import Environment, FileSystemLoader
import os
import json

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

output_dir = 'output_html'
os.makedirs(output_dir, exist_ok=True)

data = {}

with open('input.json', 'r', encoding='utf-8') as input:
    data = json.load(input)

# Iterate over each data entry and generate HTML
for key in data.keys():
    # Render the template with the current data
    user_data = data[key]

    interview_scores = user_data.get('interview ratings')
    url = user_data.get('assignment').get('url')
    if 'https://' not in url and 'http://' not in url:
        url = f"https://{url}"

    for i in range(len(interview_scores)):
        if interview_scores[i] == "":
            interview_scores[i] = 0
        else:
            interview_scores[i] *= 20

    rendered_html = template.render(
        name = user_data.get('name', 'NAME_NOT_FOUND'),
        aptitude_marks = user_data.get('aptitude').get('score'),
        aptitude_percentage = str(round(user_data.get('aptitude').get('percentage'), 2)),

        web_dev_marks = user_data.get('web development').get('score'),
        web_dev_percentage = str(round(user_data.get('web development').get('percentage'), 2)),

        python_programming_marks = user_data.get('python programming').get('score'),
        python_programming_percentage = str(round(user_data.get('python programming').get('percentage'), 2)),

        assignment_score = user_data.get('assignment').get('score'),
        submission_url = user_data.get('assignment').get('url'),
        submission_link = url,

        self_introduction_score = interview_scores[0],
        project_explanation_score = interview_scores[1],
        communication_skill_score = interview_scores[2],
        html_css_score = interview_scores[3],
        bootstrap_score = interview_scores[4],
        python_theory_score = interview_scores[5],
        python_coding_easy_score = interview_scores[6],
        python_coding_medium_score = interview_scores[7],
        python_coding_hard_score = interview_scores[8],

        web_dev_questions = user_data.get('asked questions').get('web development'),
        python_coding_questions = user_data.get('asked questions').get('python programming')
    )
    
    # Define the output file path
    output_path = os.path.join(output_dir, f"{key}.html")
    
    # Write the rendered HTML to the file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    
    print(f"Generated {output_path}")

print("All HTML files have been generated.")
