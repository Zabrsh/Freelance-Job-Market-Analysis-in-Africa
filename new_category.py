import openai
import json
import re

# Load your API key from an environment variable or secret management service
openai.api_key = ''

# Load job titles from JSON file
with open('jobs.json', 'r') as f:
    data = json.load(f)

# Regex pattern to match 'Category: ' followed by any non-whitespace characters until a period or newline
category_pattern = re.compile(r'Category: ([^.|\n]+)')
# Regex pattern to match 'Skills: ' followed by any non-whitespace characters until a period or newline
skills_pattern = re.compile(r'Skills: ([^.|\n]+)')

# Add categories and skills to the job titles
for job in data:
    job_title = job["job_title"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"This job title is a {job_title}. Please respond in the format 'Category: [job category]. Skills: [required skills]'",
        temperature=0.3,
        max_tokens=100
    )

    # Extract the job category and skills using the regex
    result_text = response.choices[0].text.strip()

    category_match = category_pattern.search(result_text)
    if category_match:
        job_category = category_match.group(1)
        job["job_category"] = job_category

    skills_match = skills_pattern.search(result_text)
    if skills_match:
        # Split skills by comma and strip white spaces
        skills = [skill.strip() for skill in skills_match.group(1).split(',')]
        job["skills"] = skills

# Save the new data to a JSON file
with open('job_titles_with_categories_and_skills.json', 'w') as f:
    json.dump(data, f)
