# Validate Me

A single use python file designed to be used to validate all other files within a workspace.

## Install

 - requirements as per requirements.txt
 - npm install -g jshint

 ## To run

A) Add to Existing project
- Add validate_me.py to your main directory
B) Clone code to be validated
- git clone https://github.com/*USERNAME*/*REPOSITORY*.git *FOLDER_NAME*
(FOLDER_NAME will be a new folder created in the workspace to hold the cloned repository)

Once you have run -
- python3 validate_me.py

## Current Features
- HTML validation
- CSS validation
- Python validation PEP8
- JavaScript validation

## To do
- Resolve JQuery for jshint
- HTML Templating for Flask/Django/Jinja

## Acknowledgements

I do not own the libraries of -
PEP8
- https://pypi.org/project/pep8/
W3 validators
- https://pypi.org/project/Online-W3C-Validator/
JSHint
- https://jshint.com/about/