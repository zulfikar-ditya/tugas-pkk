# Simple Payment Management

## How to use

### Clone Repository
> clone
```
git clone https://github.com/Zulfikar-ditya/tugas-pkk.git pkk
```

> change directory
```
cd pkk
```

### Make + Activate Virtual Environtment
> make VENV
```
python -m venv env
```
> activate VENV
```
env\Scripts\activate
```

### Install requirements
> install
```
pip -r install requirements.txt
```

### Migrations
> Make Migrations
```
manage.py makemigrations
```
> migrate
```
manage.py migrate
```

### Load Data
> load
```
manage.py loaddata data/months.json
```

### Make User + Runserver
> Make User
```
manage.py createsuperuser
```
> runserver
```
manage.py runserver
```


### enjoy