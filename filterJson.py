import json

def filter_empty_objects(json_data):
 
  filtered_objects = []
  for object in json_data:
    if object:
      filtered_objects.append(object)

  return filtered_objects


def main():
  with open("jobs.json", "r") as f:
    json_data = json.load(f)

  filtered_objects = filter_empty_objects(json_data)

  # Store the filtered objects in a JSON file.
  with open("filtered_jobs.json", "w") as f:
    json.dump(filtered_objects, f)


if __name__ == "__main__":
  main()
