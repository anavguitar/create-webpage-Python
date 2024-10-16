#Andres Avendano
#Oct 15 2024 
#Assignment 6
#CISW 24

import sys
import os
import datetime

# get the user input

file_name = input("Enter the name of the file (do not include .html extension):")
out_file = f'{file_name}.html'

body_h1 = input('Enter the character name: ')
body_h1 = f'<h1>{body_h1}</h1>\n'

body_h2 = input('Enter the actor\'s name: ')
body_h2 = f'<h2> Played by {body_h2} </h2>\n'

body_description = input('Enter a brief description of the character: ')
body_description = f'<p>{body_description}</p>\n'

body_img = input('Enter the location/path of the character\'s image: ')
body_img = f'<img src={body_img} alt="{file_name}">\n'

combined_body = body_h1 + body_h2 + body_description + body_img

page_head = open("page-head.txt", "r")
combined_head = ''.join(page_head.readlines())
page_head.close()

page_footer = open("page-footer.txt", "r")
combined_footer = ''.join(page_footer.readlines())
page_footer.close()

combined_page = combined_head + combined_body + combined_footer

f = open(out_file, 'w')
f.write(combined_page)
f.close()
print("Created {}".format(out_file))