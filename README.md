# django-aws-translation
This is a basic django project that leverages translatable for a Pages Model and AWS's boto3 translation API. 

1. Download the repo. Duh...

2. Create a virtualenvironment... if you have any problems doing that - follow this tutorial: http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/

ALERT: This is for Python3, although adapt it if you must - it's not that hard to rework it so that you get it to work in 2.7 (which is going to be deprecated at the end of the year so, just realise that)

2.1 pip install -r requirements.txt inside the /webapp/ folder.

2.2 There are fixtures for translated pages inside /webapp/pages/fixtures/initial_data.json if you're migrating your own fresh db.

2.3 Don't forget to "python manage.py createsuperuser" - so you can login to the admin area.

Ok so now that you've python manage.py runserver, and django's running. What does the project really give you.

Well firstly - look inside /admin/ - click the Pages Model, and go and add pages / edit pages etc.
You'll notice that TinyMCE is added, but also that there's a little AWS icon next to the textbox and textareas.

You'll need to go inside the settings.py file and configure these variables if you want this feature to work:
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION_NAME = 'us-east-1'
AWS_CLIENT_ID = ""

Which shouldn't be too hard provided you follow this: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

Once you have your AWS credentials setup, try click the AWS icon in the admin again, and you'll see it translates your copy using AWS and replaces it. Obviously it won't translate English. So on English, you won't see the AWS icons.

I've gone and coded a management command too:
Python manage.py translate

make sure you've removed my /webapp/locale/ folder though so it starts a fresh.

This command runs through the entire project (effectively using makemessages) and gets all the translated tag words. It then uses AWS to translate those words and creates mo files out of them. Very convenient tool - I'll give a more descriptive writeup of what that does at some later stage, but I've run out of time. 

Till next time.

Happy coding.



