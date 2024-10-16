#Andres Avendano
#Oct 15 2024 
#Assignment 6
#CISW 24

import sys
import os
import datetime

# get the user input

file_name = input("Enter the name of the file (do not include .html extension):")
out_file = open(f'{file_name}.html', 'a+')

body_h1 = input('Enter the character name: ')
body_h1 = f'<h1>{body_h1}</h1>\n'

body_h2 = input('Enter the actor\'s name: ')
body_h2 = f'<h2> Played by {body_h2} </h2>\n'

body_description = input('Enter a brief description of the character: ')
body_description = f'<p>{body_description}</p>\n'

body_img = input('Enter the location/path of the character\'s image: ')
body_img = f'<img src={body_img} alt="{file_name}">\n'

combined_body = f"""
    {body_h1}
    {body_h2}
    {body_description}
    {body_img}
"""

test = open('test.txt', 'r')
print(test.read())

page_head = open("page-head.txt", "r")
page_footer = open("page-footer.txt", "r")

print(page_head.read())
print(page_footer.read())

