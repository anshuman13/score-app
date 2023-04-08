# React application and backend for News Score calculator

## What Is This?

The application identifies a news score based on Heart rate, Respiratory Rate and Body Temprature

## Local Development

1. Clone the repository.
2. Make sure python3 and node 16 is installed in the system.
3. In the backend folder, create a virtual environment and setup the python configuration in PyCharm or another IDE.
4. Run `pip install -r requirements.txt` to install dependencies in the virtual environment
5. Run the flask server or `flask run -h localhost -p 8000`.
6. The server is now running on http://localhost:8000.

<<<<<<< HEAD
## Front end application

1. In the root folder, Run `npm install`.
2. Run `npm start` to start the front end application.
=======
## Deploy to AWS

1. Install AWS CLI and EB CLI. [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html](url)
2. From the backend folder in spoor-web-app repository, run eb init.
3. Select region as eu-north-1, rest of config can be default.
4. For deployment in dev, checkout the dev branch in git and from the backend folder in spoor-web-app

   `eb deploy spoor-backend-dev`

5. For deployment in production, checkout the main branch in git and from the backend folder in spoor-web-app

   `eb deploy spoor-backend-prod`

## Logs in AWS

1. Connect to the EC2 instance for the environment.
2. Go to folder `/var/log`.
3. `eb-engine.log` has the top level logs for deployment.
4. `cfn-init.log` has the logs for the user beanstalk scripts.
5. `app-logs/*` has the application logs.

## Test in local and generate report

1. coverage erase
2. coverage run manage.py test -v 2 --keepdb
3. coverage report
4. coverage html
>>>>>>> 06859e1 (adding backend)
