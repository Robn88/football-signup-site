navbar- taken from codestar blog

# Football Signup 

Football Signup is a site designed for people to organise and register for football events. A superuser can create an event, and users can view this event, and the current participants. They can also see if any of the participants are bringing balls, bibs and any guests. This site was inspired by my own real life problems when trying to arrange football matches, and having to use WhatsApp groups and Doodle. My idea was to try to simplify this into a site, where users can get all of the information that they require in one place.

## Features

### Index Page

### Event Detail Page

### Event Registration Page

### Unregister Page


## Testing

## Deployment

This project has been deployed to Heroku. I will detail the steps I took in order to deploy the project below:


1. First of all, log into Heroku, click on the button 'new' in the top right-hand corner, and then select 'Create new app' from the drop down menu.

2. You will then be prompted to choose a name for your project, which must be unique. In my case, the app name is football-signup. You must also choose a region- in my case I chose Europe.

3. Then, clicking on the resources tab, I entered Heroku Postgres in the add-ons search field. This is the database used for the project.

4. Next, by clicking on the 'settings' tab and then 'Reveal Config Vars', I obtained the Database URL. Moving now to Gitpod, I created a file called env.py to store all the environment variables.

5. In env.py, I then created an environment variable as can be seen below:  

    os.environ["DATABASE_URL"] = " "  

    I then put the value from the DATABASE_URL Config Var between the double quotes.

6. In env.py, I then created a new environment variable for the secret key, as can be seen below:  

    os.environ["SECRET_KEY"] =  " "  

    I then created my own secret key and put it between the double quotes.

7. I then returned to the settings section of Heroku, and created a new Config Var called SECRET_KEY, and assigned it the same value as in stage 6.

8. Next, I opened settings.py and added the following code:  

     ![deployment screenshot 1](/assets/readme/deployment/deployment_screenshot_1.png)  
    
   This is to prevent the application from throwing an error if it is unable to find the file, since it won't exist in production

9. In settings.py, I then changed the insecure key to the path to the newly created secret key.

10. Again, in settings.py, I created a python dictioanry to connect the database to the application.  

![deployment screenshot 2](/assets/readme/deployment/deployment_screenshot_2.png)

11. Returning to Heroku, I now added a new Config Var called DIASBLE_COLLECTSTATIC, and set its value to 1. This was only to allow the project to be deployed, and would be subsequently deleted.

12. I then returned to settings.py in the application and added the following code:  

![deployment screenshot 3](/assets/readme/deployment/deployment_screenshot_3.png)

13. Another thing to be added was the directory for the templates:  

![deployment screenshot 4](/assets/readme/deployment/deployment_screenshot_4.png)

14. It was then necessary to add [TEMPLATES_DIR] to the DIRS section of TEMPLATES in settings.py:  

![deployment screenshot 5](/assets/readme/deployment/deployment_screenshot_5.png)

15. Before it could be deployed, the application had to be added to ALLOWED_HOSTS. This consisted of putting the app name, followed by .herokuapp.com. I also put 'localhost', in order to allow me to run the project locally.  

![deployment screenshot 6](/assets/readme/deployment/deployment_screenshot_6.png)

16. The next step was to create the Procfile, in the base directory of the app. The purpose of this was to  declare to Heroku that my application would accept http traffic, and to use Gunicorn, the production web server.

17. Following that, I added and committed the files to my GitHub repository.

18. Once this was done, I returned to Heroku, and clicked on the Deploy tab. I then selected GitHub as the deployment method.

19. When I had connected my GitHub account, I then used the search function and found the name of my repository. I then clicked on deploy branch to deploy my project.


## Credits