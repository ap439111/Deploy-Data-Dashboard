# Deploy-Data-Dashboard

This project deploys data dashboard to web

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

# go into the 5_deployment folder with:
     cd DeployDataDashboard
     
# create a procfile with the command
     touch Procfile
    and put the following in the Procfile
    web gunicorn worldbank:app
     
     pip freeze > requirements.txt
     git init
     git add .
     git config --global user.email something@email.com
     git config --global user.name "john"
     git commit -m "first commit"
     heroku create undatadash
     git remote -v
     git push heroku master


Check: https://undatadash.herokuapp.com/
