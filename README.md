## Deploy-Data-Dashboard

This project deploys data dashboard to web

# Files/Folders in the folder DeployDataDashboard
    I. Data: This folder contains UNdata_Export_20200922_021257174.csv 
    II. myapp: This folder contains following file/folders:
               i.   templates: this fodler contains index.html file
               ii.  static/img: contains logo of lindedIn and GitHub
               iii. routes.py
               iv.  __init__.py
  

# Go to www.heroku.com and create an account if you haven't already.

# install virtual environment
    
     pip3 install virtualenv
     virtualenv --python=/usr/bin/python3 venv
     source venv/bin/activate
# install libraries
     pip install flask pandas plotly gunicorn
     
# install the heroku command line tools with the following command:
    
    curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
    https://devcenter.heroku.com/articles/heroku-cli#standalone-installation
    
     heroku --version
     
# command line login to heroku
     heroku login -i
     and then enter your email and password when asked

# go into the DeployDataDashboar folder with:
     cd DeployDataDashboard
     
# create a procfile with the command:
    > touch Procfile
    
    and put the following in the Procfile
    
    > web gunicorn worldbank:app
     
#  create a requirements file with this command:

     pip freeze > requirements.txt
     
# initialize a git repository with the following commands:
     git init
     git add .
     
# configure the email and user name, you can use these commands:
     git config --global user.email something@email.com
     git config --global user.name "john"
     
# make a commit with this command:
     git commit -m "first commit"
     
# create a uniquely named heroku app. Use this command:
     heroku create undatadash
     
     If you get a message that the app name is already taken, try again with a different app name until you find one that is not taken.
# Check that heroku added a remote repository with this command:     
     git remote -v
#  push the app to Heroku:
     git push heroku master
     
# Go to the link for your web app to see if it's working. The link should be:
    Check: https://undatadash.herokuapp.com/
