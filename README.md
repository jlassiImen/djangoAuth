DjangoAuth
Ce projet permet aux utilisateurs de se connecter ,accèder à une page pour afficher/modifier son adresse email .

Prérequis:
-Python 2.7
-Django 1.8

Commencer:
1. Clonez le référentiel:
git clone https://github.com/jlassiImen/djangoAuth
2. Exécutez les migrations:
python manage.py migrate
3. Créer un user:
python manage.py createsuperuser
4. Exécuter le serveur:
python manage.py runserver
5. Et ouvrez  http://127.0.0.1:8000/account/login dans votre navigateur Web.


Deploiement sur Docker
1. Exécuter:
> sudo  docker build -t django-auth .
> sudo docker run -p 8000:8000 -i -t  django-auth
ouvrez http://127.0.0.1:8000/account/login dans votre navigateur Web.

Compte par défault: usernmae = admin, password = admin

Author
JLASSI Imen
