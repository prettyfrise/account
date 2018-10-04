# account

## Github SSL connect error
 * git version up 2.18
  * rpm -Uvh http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm
  * yum --enablerepo=WANdisco-git --disablerepo=base,updates install git
  * yum update -y nss curl
  
## System PATH
```
PATH=$PATH:$HOME/bin:/root/app/pytho3/bin
export LD_LIBRARY_PATH=$HOME/app/pytho3/lib:$LD_LIBRARY_PATH
alias run='python3 /root/accountbook/manage.py runserver 0.0.0.0:8000'
```
## Databases setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'account',
        'USER': 'root',
        'PASSWORD': 'Ehfkeh23..',
        'HOST': 'localhost',
        'PORT': '13306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
```

## create admin User
* python manage.py createsuperuser


