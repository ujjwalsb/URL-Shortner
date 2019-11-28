![Project](https://img.shields.io/badge/Project-URL%20Shortening%20Services-brightgreen.svg)
![Company](https://img.shields.io/badge/Company-InstaCAR-green.svg)
![Languages Python](https://img.shields.io/badge/Languages-Python,%20JavaScript,%20HTML,%20CSS-blue.svg)
![Framework Django](https://img.shields.io/badge/Framework-Django-yellow.svg)
![Status Complete](https://img.shields.io/badge/Status-Complete-orange.svg)

### URL Shortening Service (Documentation)

----------------

**The project is hosted on the free hosting providor *`www.pythonanywhere.com`*.**

*Project Link -* [http://projectassignment.pythonanywhere.com](http://projectassignment.pythonanywhere.com/)

*Analytics Link-* [http://projectassignment.pythonanywhere.com/analytics](http://projectassignment.pythonanywhere.com/analytics/)

*Admin Link-* [http://projectassignment.pythonanywhere.com/admin](http://projectassignment.pythonanywhere.com/admin/)

`User ID - url`
`Password - url`

----------------

**"URL Shortening service is a web application where you can enter any of your long URL/Link and make it short, thus making your Link sharable anywhere and it'll be redirected to your original Domain."**

----------------

#### Steps to run this project on Docker:


1. Clone the repository `URL-Shortner` on your local dev machine.

	```$ git clone https://github.com/ujjwalsb/URL-Shortner.git```
    
2. Get inside the root directory of the project.

	```$ cd URL-Shortner/url_shortning_service```

3.  You may find all files and folders inside, but we need to look for the *Docker* file.

	`Dockerfile & docker-compose.yml`

	These 2 files are responsible to setup you project on Docker under your local dev
    machine to get your project up and running hasle free.
    
4. Being in your current directory & assuming the docker has already been installed. [(If not, follow this)](https://docs.docker.com/v17.09/engine/installation/#time-based-release-schedule), run the following commands to check the version & verify its installation:

	```$ docker-compose -v```
    
5. Now everything has been setup, you can directly enter the following commands in your terminal:

	```$ docker-compose up```

**Now, sit back and relax while the all the necessary images are being pulled as mentioned on the `Dockerfile` and after that let it automatically perform all executable steps from `docker-compose.yml`.**

6. After the above steps are are done, you may see the following project running logs-

	```
    Starting url_shortner ... done
    Attaching to url_shortner
    url_shortner | No changes detected
	url_shortner | Operations to perform:
	url_shortner |   Apply all migrations: admin, auth, contenttypes, sessions, url_shortner
	url_shortner | Running migrations:
	url_shortner |   No migrations to apply.
	url_shortner | Performing system checks...
	url_shortner | 
	url_shortner | System check identified no issues (0 silenced).
	url_shortner | November 28, 2019 - 05:36:37
	url_shortner | Django version 2.2.7, using settings 'url_shortning_service.settings'
	url_shortner | Starting development server at http://0.0.0.0:8000/
	url_shortner | Quit the server with CONTROL-C. 
    ```
    
7. Open your browser and access `http://localhost:8000` or `127.0.0.1:8000` and your project will be running.

8. Now, as soon as you click or start running your project the logs will be continued on the terminal screen.
To get rid of the logs on the screen and run the project in detached mode **(background mode)** where you can just `start & stop the services`, follow the commands below.

	`Docker-compose start` --> To start the project in background.
    
    `Docker-compose stop` --> To stop the background service of the app.
    
    `Docker-compose restart` --> To restart the running service on background.
    
    
----------------

**Project Link -** ```http://projectassignment.pythonanywhere.com/```

---------------

