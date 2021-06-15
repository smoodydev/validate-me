import requests
import pep8
import os
from w3c_validator import validate as cssval
import subprocess as commands


def checkPython(f):
    return pep8.Checker(f).check_all()


def checkCSS(f):
    cssissues = cssval(f)["messages"]
    for mess in cssissues:
        print(mess)
    return len(cssissues)


def checkHTML(f):
    r = requests.post(
        'https://validator.w3.org/nu/',
        data=open(f, 'rb').read(),
        params={'out': 'json'},
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' +
                 '(KHTML, like Gecko) Chrome/41.0.2272.101    ' +
                 'Safari/537.36',
                 'Content-Type': 'text/html; ' +
                 'charset=UTF-8'})
    messages = r.json()["messages"]
    error_count = 0
    if messages:
        for message in messages:
            if message["type"] == "error":
                error_count += 1
                print(f)
                print(message)
    return [error_count, len(messages)-error_count]


def validate_me():
    issues_found = 0
    html_warnings = 0
    file_arr = os.listdir()
    file_arr.remove(".git")
    for f in file_arr:
        if f[-3:] == ".py":
            issues_found += checkPython(f)
        elif f[-4:] == ".css":
            issues_found += checkCSS(f)
        elif f[-3:] == ".js":
            cmd = 'jshint %s'
            giggle = (commands.getstatusoutput(cmd % f))

        elif f[-5:] == ".html":
            htmlissues = checkHTML(f)
            issues_found += htmlissues[0]
            html_warnings += htmlissues[1]
        elif os.path.isdir(f):
            for x in os.listdir(f):
                file_arr.append(f+"/"+x)
    print(issues_found)
    print("Html Warnings: " + str(html_warnings))

if __name__ == "__main__":
    validate_me()
