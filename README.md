# DeliveryJet
# create environment 
-Set-ExecutionPolicy Unrestricted -Scope Process
-python -m venv ENV
-.\ENV\Scripts\activate


# go to inside the project
-cd DeliveryJet

# install
-python -m pip install django
-python -m pip install pillow
-python -m pip install django-ckeditor
-python -m pip install django-filter
-python -m pip install django-widget-tweaks

# run the server
-python .\manage.py runserver
