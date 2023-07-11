import re
import os

def make_consistent(data):

  # Standardize the capitalization.
  #   data = data.lower()

  # Standardize the spacing.
  data = re.sub(' +', ' ', data)
  data = re.sub('\n\n+', '\n', data)
  # Standardize the indentation.
  #   data = re.sub('\t', '    ', data)
  data = data.replace('**Job Title:**', 'Job Title:')
  data = data.replace('**Job Type:**', 'Job Type:')
  data = data.replace('**Work Location:**', 'Work Location:')
  data = data.replace('**Description**:', 'Description:')
  data = data.replace('for our amharic channel, join @afriworkamharic:', ' ')
  data = data.replace('From: @freelance_ethio | @freelanceethbot',' ')
  data = data.replace('For our Amharic Channel, Join @afriworkamharic', ' ')
  data = data.replace('- - - - - - - - Closed - - - - - - - -', ' ')
  
  return data

def read_data_from_file(filename):
 

  with open(filename, 'r', encoding='utf-8') as f:
    data = f.read()

  return data

def write_data_to_file(data, filename):


  with open(filename, 'w', encoding='utf-8') as f:
    f.write(data)

if __name__ == '__main__':
  filename = 'messages.txt'
  data = read_data_from_file(filename)
  consistent_data = make_consistent(data)
  write_data_to_file(consistent_data, 'consistent_data.txt')
