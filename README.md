# Deploy-Data-Dashboard

This project deploys data dashboard to web

#Steps to upload 

     pip3 install virtualenv
     virtualenv --python=/usr/bin/python3 venv
     source venv/bin/activate
     pip install flask pandas plotly gunicorn
     heroku --version
     heroku login -i
     touch Procfile
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
