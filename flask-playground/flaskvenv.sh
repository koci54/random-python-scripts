#!/bin/bash -e

# Create a minimal flask project

if [ $# -ne 1 ]; then
    echo $0: "usage: source ./flaskvenv.sh <name>"
    exit 1
fi

projectname=$1

# Python 3.3+
python3 -m venv "${projectname}"

# Activate the virtualenv (OS X & Linux)
source $(pwd)"/${projectname}/bin/activate"

#install flask 
pip install flask

# create minimal flask app
touch ${projectname}.py

# append lines
echo "from flask import Flask" >> ${projectname}.py
echo "app = Flask(__name__)" >> ${projectname}.py
echo "app.config['"DEBUG"'] = True" >> ${projectname}.py
echo "@app.route('"\/"')" >> ${projectname}.py
echo "def hello_world():" >> ${projectname}.py
echo "    return '<p>Hello, World!</p>'" >> ${projectname}.py

touch run-flask-app.sh
chmod a+x ./run-flask-app.sh

echo "#!/bin/bash -e" >> run-flask-app.sh
echo "export FLASK_APP=${projectname}" >> run-flask-app.sh
echo "flask run -h localhost -p 5001" >> run-flask-app.sh

# open a new terminal window and run the newly created script
