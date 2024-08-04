## Before running code, please change the value of root_dir and output_dir to the correct paths. 

import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
message_list = []

root_dir =  
output_dir =  
for file in os.listdir(root_dir):
    json_path = os.path.join(root_dir, file)
    if os.path.exists(json_path):
         with open(json_path, "r", encoding="utf-8") as message_file:
            message_data = json.load(message_file)
            for message in message_data:
                    message_author = message.get("author")
                    message_sender = message_author.get("username")
                    message_content = message.get("content", "Unretrieved")
                    if not message_content or message_content.isspace():
                            message_content = "Unretrieved"
                    try:  
                        message_list.append(f"{message_sender}: {message_content}")
                    except UnicodeEncodeError:
                        message_content = "Encoding Error"
                        message_list.append(f"{message_sender}: Encoding Error")
                    
message_list.reverse() 

with open(output_dir, "w", encoding="utf-8") as output_file:
    for x in message_list:
        output_file.write(f"{x} \n")
print("Done!") 
