import os
import re
import sys


def mdToHtml(line):

    line = re.sub(r'^#\s(.*?)$', r'<h1>\1</h1>', line)
    line = re.sub(r'^##\s(.*?)$', r'<h2>\1</h2>', line)
    line = re.sub(r'^###\s(.*?)$', r'<h3>\1</h3>', line)

    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)
    
    line = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', line)
    line = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', line)
    
    line = re.sub(r'[^!]\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
    
    line = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', line)
    
    
    return line

def main(file):
    with open(file, 'r') as f:
        md_file = f.readlines()
        
    with open("output.html", "w") as html_file:
        

        for line in md_file:
            html_line = mdToHtml(line)
            html_file.write(html_line)

        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erro no ficheiro md")
    else:
        main(sys.argv[1])