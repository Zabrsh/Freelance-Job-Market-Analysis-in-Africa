import re
import json

def extract_job_details(text):
  """Extracts the job title, job type, job description, and job location from the given text.

  Args:
    text: The text to extract the job details from.

  Returns:
    A dictionary containing the job title, job type, job description, and job location.
  """

  job_details = {}

  # Extract the job title.
  job_title_match = re.search(r"Job Title:\s*(.+)", text, flags=re.IGNORECASE)
  if job_title_match:
    job_details["job_title"] = job_title_match.group(1)

  # Extract the job type.
#   job_type_match = re.search(r"Job Type:\s*(.+)", text, flags=re.IGNORECASE)
#   if job_type_match:
#     job_details["job_type"] = job_type_match.group(1)

  # Extract the job description.
#   job_description_match = re.search(r"Job Description:\s*(.+)", text, flags=re.IGNORECASE)
#   if job_description_match:
#     job_details["job_description"] = job_description_match.group(1)

  # Extract the job location.
#   job_location_match = re.search(r"Work Location:\s*(.+)", text, flags=re.IGNORECASE)
#   if job_location_match:
#     job_details["job_location"] = job_location_match.group(1)

  return job_details


def main():
  text = open("consistent_data.txt", "r", encoding='utf-8').read()

  job_details = []
  for line in text.splitlines():
    if not re.search(r"[\u1200-\u137F]", line):
      job_details.append(extract_job_details(line))

  # Store the extracted data in a JSON file.
  json_data = json.dumps(job_details)
  with open("jobs.json", "w") as f:
    f.write(json_data)


if __name__ == "__main__":
  main()
