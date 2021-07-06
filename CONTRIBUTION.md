# Contribution Guidelines 
Guidelines for contributing to this project. Must be strictly followed by all team members.  
This will guide you from cloning this repository to pushing your contributions.

## Forking
Fork this repository to get a personal copy on your github account

## Cloning
To clone the forked repository to your local machine, open command prompt and run:
```
git clone https://github.com/your-account-name/e-care-be-pjt-6
```

## Change to project directory
Change to the project directory you just cloned
```
cd e-care-be-pjt-6
```

## Set Upstream Remote
To set upstream remote so you can pull changes from upstream to update your repo run:
```
git remote add upstream https://github.com/zuri-training/e-care-be-pjt-6
```

## Checkout Develop Branch
Checkout develop branch by running
```
git checkout develop
```

## Checkout Your Feature Branch
Feature Branching Workflow means you create a new branch for every feature or issue you are working on.
It is goood practice for the branch name to end with the issue id.
So if an issue id is **#5** and issue name is **Signup API** then our branch name would be **signup-api-#5**.
create and checkout feature branch by running:
```
git checkout -b issue-name-id
```

## Setup Development Environment
To setup the development environment to run project run:
```
pipenv install
```

## Migrate Database
Migrate the database by running:
```
python manage.py migrate
```

## Set Environment Variables
Create a **.env** file and add the following config vars:
```
SECRET_KEY=Averyrandomstringthatwillbehardforanyonetoguessevenyou
DEBUG=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
save the file.

## Run Project
If you want to test the development environment run:
```
python manage.py runserver
```

# When You Have Fixed The Issue
When you have finished making changes and have commited your changes.

## Pull Update from Remote
Pull latest update from the upstream remote repo by running:
```
git pull upstream develop
```

## Push Local Changes to origin
Push your new fix or feature to the remote branch of your feature.
If your feature branch name is **signup-api-#5** then run:
```
git push origin signup-api-#5
```

## Make PR
Goto your github account and make a **Pull Request** to merge your changes to upstream.

## Happy Contributing!!!
