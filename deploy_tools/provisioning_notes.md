Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git


## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

* ### Turn selinux to permissive

## Adding site blocks to NGINX

* Add sites-available and sites-enabled folders to /etc/nginx
* Create server config file in sites-available and symlink to sites-enabled
* add sites-enabled folder to nginx.conf, copy the style of the conf.d/*.conf include in http block

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

Provide read permissions to NGINX user to static folder

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
