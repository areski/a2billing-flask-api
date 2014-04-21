#!/bin/bash
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2014 Star2Billing S.L.
#
# The Initial Developer is
# Arezqui Belaid <info@star2billing.com>
#

#
# To download and run the script on your server :
# cd /usr/src/ ; wget --no-check-certificate https://raw.github.com/areski/a2billing-flask-api/master/install/install.sh -O install.sh ; bash install.sh
#

INSTALL_MODE='CLONE'
INSTALL_DIR='/usr/share/a2billing-flask-api'
INSTALL_ENV="a2billing-flask-api"
HTTP_PORT="8008"

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

#Include general functions
wget --no-check-certificate https://raw.github.com/areski/a2billing-flask-api/master/install/bash-common-functions.sh -O bash-common-functions.sh
source bash-common-functions.sh

#Identify the OS
func_identify_os



#Fuction to create the virtual env
func_setup_virtualenv() {
    echo "This will install virtualenv & virtualenvwrapper"
    echo "and create a new virtualenv : $INSTALL_ENV"

    echo "Press enter to continue"
    read TEMP

    easy_install virtualenv
    easy_install virtualenvwrapper

    # Enable virtualenvwrapper
    chk=`grep "virtualenvwrapper" ~/.bashrc|wc -l`
    if [ $chk -lt 1 ] ; then
        echo "Set Virtualenvwrapper into bash"
        echo "export WORKON_HOME=/usr/share/virtualenvs" >> ~/.bashrc
        echo "source $SCRIPT_VIRTUALENVWRAPPER" >> ~/.bashrc
    fi

    # Setup virtualenv
    export WORKON_HOME=/usr/share/virtualenvs
    source $SCRIPT_VIRTUALENVWRAPPER

    mkvirtualenv $INSTALL_ENV
    workon $INSTALL_ENV

    echo "Virtualenv $INSTALL_ENV created and activated"

    echo "Press enter to continue"
    read TEMP

}


#Function to configure Apache
func_configure_http_server(){
    # prepare Apache
    echo "Prepare Apache configuration..."

    echo "Press enter to continue"
    read TEMP

    echo '
    '$WSGI_ADDITIONAL'

    Listen *:'$HTTP_PORT'

    <VirtualHost *:'$HTTP_PORT'>
        DocumentRoot '$INSTALL_DIR'/
        ErrorLog /var/log/a2billing-flask-api/err-apache-a2billing_flask_api.log
        LogLevel warn

        WSGIPassAuthorization On
        WSGIDaemonProcess a2billing_flask_app user='$APACHE_USER' user='$APACHE_USER' threads=25
        WSGIProcessGroup a2billing_flask_app
        WSGIScriptAlias / '$INSTALL_DIR'/a2billing_flask_app.wsgi

        <Directory '$INSTALL_DIR'>
            WSGIProcessGroup a2billing_flask_app
            WSGIApplicationGroup %{GLOBAL}
            AllowOverride all
            Order deny,allow
            Allow from all
            '$WSGIApplicationGroup'
        </Directory>

    </VirtualHost>
    ' > $APACHE_CONF_DIR/a2billing_flask_app.conf
    #correct the above file
    sed -i "s/@/'/g"  $APACHE_CONF_DIR/a2billing_flask_app.conf

    echo "Restart HTTP Server"
    service $APACHE_SERVICE restart

    echo "Press enter to continue"
    read TEMP
}


#Configure Logs files and logrotate
func_prepare_logger() {
    echo ""
    echo "Prepare logger..."
    echo "Press enter to continue"
    read TEMP

    mkdir /var/log/a2billing-flask-api/
    touch /var/log/a2billing-flask-api/err-apache-a2billing_flask_api.log
    touch /var/log/a2billing-flask-api/a2billing_flask_api.log
    chown -R $APACHE_USER:$APACHE_USER /var/log/a2billing-flask-api

    rm /etc/logrotate.d/a2billing_flask_api
    touch /etc/logrotate.d/a2billing_flask_api
    echo '
/var/log/a2billing-flask-api/*.log {
        daily
        rotate 10
        size = 50M
        missingok
        compress
    }
'  > /etc/logrotate.d/a2billing_flask_api

    logrotate /etc/logrotate.d/a2billing_flask_api
}


#Function to install Frontend
func_install() {
    echo ""
    echo "We will now install a2billing-flask-api on your server"
	echo "======================================================"
    echo ""
    echo "Press enter to continue"
    read TEMP

    #python setup tools
    echo "Install Dependencies and Python modules..."
    echo ""
    case $DIST in
        'DEBIAN')
            apt-get -y install python-setuptools python-dev build-essential git-core mercurial gawk
            easy_install pip
            apt-get -y install libapache2-mod-python libapache2-mod-wsgi
            apt-get -y install libmysqld-dev
        ;;
        'CENTOS')
            if [ "$INSTALLMODE" = "FULL" ]; then
                yum -y update
            fi
            yum -y install autoconf automake bzip2 cpio curl curl-devel curl-devel expat-devel fileutils gcc-c++ gettext-devel gnutls-devel libjpeg-devel libogg-devel libtiff-devel libtool libvorbis-devel make ncurses-devel nmap openssl openssl-devel openssl-devel perl patch unzip wget zip zlib zlib-devel policycoreutils-python

            if [ ! -f /etc/yum.repos.d/rpmforge.repo ];
            	then
                	# Install RPMFORGE Repo
        			if [ $KERNELARCH = "x86_64" ]; then
						rpm -ivh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86_64.rpm
					else
						rpm -ivh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.i686.rpm
					fi
        	fi

        	yum -y --enablerepo=rpmforge install git-core

            #Install epel repo for pip and mod_python
            if [ $KERNELARCH = "x86_64" ]; then
				rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-7.noarch.rpm
			else
				rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-7.noarch.rpm
			fi

            # disable epel repository since by default it is enabled.
            sed -i "s/enabled=1/enable=0/" /etc/yum.repos.d/epel.repo
            yum -y --enablerepo=epel install python-pip mod_python python-setuptools python-tools python-devel mercurial mod_wsgi libevent libevent-devel
        ;;
    esac

    #Create and enable virtualenv
    func_setup_virtualenv

    echo "Install a2billing-flask-api..."
    echo "Press enter to continue"
    read TEMP

    cd /usr/src/
    rm -rf a2billing-flask-api

    #Configure Logs files and logrotate
    func_prepare_logger

    case $INSTALL_MODE in
        'CLONE')
            git clone git://github.com/areski/a2billing-flask-api.git
        ;;
    esac

    # Copy files
    cp -rf /usr/src/a2billing-flask-api/a2billing_flask_api $INSTALL_DIR

    # Update Secret key
    echo "Update Secret Key..."
    RANDPASSW=`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 50)`
    sed -i "s/THE_SECRET_KEY/$RANDPASSW/g" /usr/share/a2billing-flask-api//usr/share/a2billing_flask_api.py

    #Install depencencies
    easy_install -U distribute
    echo "Install requirements..."
    for line in $(cat /usr/src/a2billing-flask-api/requirements.txt)
    do
        pip install $line
    done

    #Fix permission on python-egg
    mkdir $INSTALL_DIR/.python-eggs

    #Configure Logs files and logrotate
    func_configure_http_server

    #Run Gunicorn and Flask
    # /usr/share/virtualenvs/a2billing-flask-api/bin/python /usr/share/virtualenvs/a2billing-flask-api/bin/gunicorn a2billing_flask_api:app -c /usr/share/a2billing_flask_api/gunicorn.conf.py

    echo ""
    echo "*************************************************************"
    echo "Congratulations, A2Billing-Flask-API Server is now installed!"
    echo "*************************************************************"
    echo ""
    echo ""
    echo "You should now edit /usr/share/a2billing-flask-api/a2billing_flask_api.py"
    echo "and enter the right DB settings to connect to your A2Billing Database"
    echo "See the file /etc/a2billing.conf"
    echo ""
    echo "Example of common settings:"
    echo ""
    echo "DATABASE = {"
    echo "    'name': 'a2billing14',"
    echo "    'engine': 'peewee.MySQLDatabase',"
    echo "    'user': 'a2bdbuser',"
    echo "    'passwd': 'a2bdbpassw',"
    echo "}"
    echo ""
    echo "Restart Apache:"
    echo "/etc/init.d/apache2 restart"
    echo ""
    echo "After this you will need to create a new admin user."
    echo "To create a new admin user refer to the documentation of the project README.rst"
    echo ""
    echo ""
}


#run Install
func_install
