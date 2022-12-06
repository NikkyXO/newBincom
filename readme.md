Bincom Interview Test

Procedure to startup

Using Virtual Environment
- Create a Virtual Environment
- Activate the virtual environment
- Install project dependency using "pip install -r requirements.txt"


To Avoid Errors during migrations cause the models was generated from "python manage.py inspectDB > models",

- Open the base.py in the settings folder and comment the base in the INSTALLED_APPS list
- save file and run "python manage.py migrate" in the console
- Uncomment the base in the INSTALLED_APPS, save file and run "python manage.py migrate --fake"


Database
After successfully, restoring the MYSQL database file,
- Open dev.py in the settings folder, scroll to the database section and input the restored database info



Runnig server
- python manage.py runserver

Creating User
- python manage.py createsuper 


Accessing Django shell prompt
- python manage.py shell

