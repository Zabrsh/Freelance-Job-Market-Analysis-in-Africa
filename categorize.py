import openai
import json
import re

# Load your API key from an environment variable or secret management service
openai.api_key = ''

# Load job titles from JSON file
with open('filtered_jobs.json', 'r') as f:
    data = json.load(f)

# Regex pattern to match 'Category: ' followed by any non-whitespace characters
pattern = re.compile(r'Category: (\S+)')

# Add categories to the job titles
for job in data:
    job_title = job["job_title"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"This job title is a {job_title}. Please respond in the format 'Category: [job category]'",
        temperature=0.3,
        max_tokens=60
    )

    # Extract the job category using the regex
    result_text = response.choices[0].text.strip()
    match = pattern.search(result_text)
    if match:
        job_category = match.group(1)
        job["job_category"] = job_category

# Save the new data to a JSON file
with open('job_titles_with_categories.json', 'w') as f:
    json.dump(data, f)
