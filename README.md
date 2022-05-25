## Linux instructions::

**Create virtual environment:**
  
```
virtualenv venv
```

**Activate the environment**

```
source venv/bin/activate
```

**Install requirements:**

```
pip install -r requirements.txt
```

**Make migrations**

```
python manage.py makemigrations
python manage.py migrate
```

**To run server:**

```
python manage.py runserver
```

You should see that the server started properly
