import requests
import time 
import subprocess
from bs4 import BeautifulSoup

# Make a GET request to the website
response = requests.get("https://www.kooora.com/")

# Parse the HTML content using html5lib
soup = BeautifulSoup(response.content, 'html.parser')

script_tag = soup.find('script', string=lambda text: text and 'match_box = new Array (' in text)
script_content = script_tag.string

if script_tag is None:
	error_message = "Unfortunatey, no matches to display, Yassa."
	subprocess.run(['notify-send', error_message])
else:
	start_string = 'match_box = new Array ('
	end_string = 'var video_list'

	start_index = script_content.find(start_string)
	end_index = script_content.find(end_string, start_index)

	content_between_strings = script_content[start_index + len(start_string):end_index].strip()
	#print (content_between_strings)

	lines = content_between_strings.split('"#')
	lines = [line.strip() for line in lines]
	lines = list(filter(None, lines))
	#print('\n\n'.join(lines))

	# Initialize an empty list to hold the line arrays
	output_list = []
	messages = []
	# Loop through each line and split it into an array using the comma as the separator
	for line in lines:
		line_array = line.split(',')
		# Remove double quotes from each element in the line_array
		line_array = [element.replace('"', '') for element in line_array]
		output_list.append(line_array[7] + ' (' + line_array[14] + '-' + line_array[15] + ') ' + line_array[10] )
	    
		# Check if the 14th or 15th element is -1 and replace it with '-'
		if line_array[14] == '-1' or line_array[15] == '-1':
			line_array[14] = line_array[18]
			line_array[15] = line_array[19]
			if line_array[14] == '-1' or line_array[15] == '-1':
				line_array[14] = '-'
				line_array[15] = '-'
				message = f" 🔘 {line_array[7]} ({line_array[14]}-{line_array[15]}) {line_array[10]}"
				messages.append(message)
			else :	
				message = f" 🔴 {line_array[7]} ({line_array[14]}-{line_array[15]}) {line_array[10]}"
				messages.append(message)
		else :	
			message = f" 🟢 {line_array[7]} ({line_array[14]}-{line_array[15]}) {line_array[10]}"
			messages.append(message)



	    # Print the 4th, 10th, 14th, and 15th elements of each array
		#print(line_array[7], '(',line_array[14],"-",line_array[15],')', line_array[10])  
	output_string = '\n'.join([','.join(line) for line in output_list])
	# print(output_list)

	# Join all the messages into a single string
	notification_message = "\n".join(messages)

	# Run the notify-send command for the notification message
	print(notification_message)
	subprocess.run(['notify-send', notification_message])