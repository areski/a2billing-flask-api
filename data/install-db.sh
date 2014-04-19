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

#
# To download and run the script on your server :
# cd /usr/src/ ; wget --no-check-certificate https://raw.github.com/areski/a2billing-flask-api/master/data/install-db.sh -O install-db.sh ; bash install-db.sh
#

sudo apt-get install mysql-server

USER='root'
PASSW='password'
DBPASS='password'
DBUSER='root'
DBNAME='a2billing_db'
HOSTNAME='localhost'
MYSQL -u $USER -h -p$PASSW -Bse "CREATE DATABASE $DBNAME;"
MYSQL -u $USER -h -p$PASSW -Bse "GRANT ALL ON $DBUSER.* to  $DBNAME identified by $DBPASS;"

cat a2billing_db.mysql| mysql --user=$USER --password=$PASSW --host=$HOSTNAME $DBNAME
