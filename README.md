DjangoAuth
Ce projet permet aux utilisateurs de:
• Se connecter.
• Accèder à une page pour afficher / modifier ses informations.
• Modifier l'adresse email en cliquant sur "Modifier ses informations" un modal qui s'ouvre pour faire la modification. Ce modal contient un input permettant de modifier l'adresse email, ainsi qu'un bouton "enregistrer". A l'appui de ce bouton, l'adresse email sera modifiée dans la base de données et sur la page principale sans rechargement de la page.

Commencer:
1. Clonez le référentiel:
git clone https://github.com/jlassiImen/djangoAuth
2. Exécutez les migrations:
python manage.py migrate
3. Créer un user:
python manage.py createsuperuser
4. Exécuter le serveur:
python manage.py runserver
5. Et ouvrez 127.0.0.1:8000/account/login dans votre navigateur Web.

Deployment Docker
1. Exécuter:
sudo  docker build -t my-django-app .
2. Exécuter:
sudo docker run -p 8000:8000 -i -t  my-django-app 

Author
JLASSI Imen
