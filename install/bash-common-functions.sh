#!/bin/bash
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2014 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

DATETIME=$(date +"%Y%m%d%H%M%S")
KERNELARCH=$(uname -p)
SCRIPT_NOTICE="This script is only intended to run on Ubuntu LTS 10.04 / 12.04 / 14.04 or CentOS 6.2"


# Identify Linux Distribution type
func_identify_os() {

    if [ -f /etc/debian_version ] ; then
        DIST='DEBIAN'
        if [ "$(lsb_release -cs)" != "lucid" ] && [ "$(lsb_release -cs)" != "precise" ] && [ "$(lsb_release -cs)" != "wheezy" ]; then
		    echo ""
		    exit 255
	    fi
    elif [ -f /etc/redhat-release ] ; then
        DIST='CENTOS'
        if [ "$(awk '{print $3}' /etc/redhat-release)" != "6.2" ] ; then
        	echo $SCRIPT_NOTICE
        	exit 255
        fi
    else
        echo ""
        echo $SCRIPT_NOTICE
        echo ""
        exit 1
    fi

    #Prepare settings for installation
    case $DIST in
        'DEBIAN')
            SCRIPT_VIRTUALENVWRAPPER="/usr/local/bin/virtualenvwrapper.sh"
            APACHE_CONF_DIR="/etc/apache2/sites-enabled/"
            APACHE_USER="www-data"
            APACHE_SERVICE='apache2'
            WSGI_ADDITIONAL=""
            WSGIApplicationGroup=""
        ;;
        'CENTOS')
            SCRIPT_VIRTUALENVWRAPPER="/usr/bin/virtualenvwrapper.sh"
            APACHE_CONF_DIR="/etc/httpd/conf.d/"
            APACHE_USER="apache"
            APACHE_SERVICE='httpd'
            #WSGI_ADDITIONAL="WSGISocketPrefix run/wsgi"
            WSGI_ADDITIONAL="WSGISocketPrefix        /var/run/wsgi"
            WSGIApplicationGroup="WSGIApplicationGroup %{GLOBAL}"
        ;;
    esac
}


#Function mysql db setting
func_get_mysql_database_setting_asteriskcdrdb() {
    if mysql -u$MYSQLUSER -p$MYSQLPASSWORD -P$MYHOSTPORT -h$MYHOST $DATABASENAME -e ";" ; then
        #Database settings correct
        echo "Mysql settings correct!"
    else
        echo ""
        echo "Configure Mysql Settings to connect to the A2Billing Database..."
        echo ""

        echo "Enter Mysql hostname (default:localhost)"
        read MYHOST
        if [ -z "$MYHOST" ]; then
            MYHOST="localhost"
        fi
        echo "Enter Mysql port (default:3306)"
        read MYHOSTPORT
        if [ -z "$MYHOSTPORT" ]; then
            MYHOSTPORT="3306"
        fi
        echo "Enter Mysql Username (default:root)"
        read MYSQLUSER
        if [ -z "$MYSQLUSER" ]; then
            MYSQLUSER="root"
        fi
        echo "Enter Mysql Password (default:password)"
        read MYSQLPASSWORD
        if [ -z "$MYSQLPASSWORD" ]; then
            MYSQLPASSWORD="password"
        fi
        echo "Enter Database name (default:asteriskcdrdb)"
        read DATABASENAME
        if [ -z "$DATABASENAME" ]; then
            DATABASENAME="asteriskcdrdb"
        fi
    fi
}
