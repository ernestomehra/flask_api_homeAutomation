from flask import Flask
import markdown
import os

#Create an instance of flask
app = Flask(__name__)

@app.route('/')
def read_me():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

    #Convert to HTML
    return markdown.markdown(content)


