#!/bin/bash -

# Copyright (c) 2014 Martin Abente Lahaye. - tch@sugarlabs.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software

bundles="${@:1}"

json=./etc/bundles.json

user="$(./helpers/get_key.py -p ${json} -k user)"
server="$(./helpers/get_key.py -p ${json} -k server)"
path="$(./helpers/get_key.py -p ${json} -k path)"

root="$(./helpers/get_key.py -p ${json} -k root)"
url="$(./helpers/get_key.py -p ${json} -k url)"

echo "Uploading to:"
echo -e '\t'$user@$server:$path/bundles/

echo "Bundles:"
for bundle in $bundles;
do
    echo -e '\t'$(basename $bundle)
done

echo "Please type \"confirm\" to continue..."
read confirm

if [ "$confirm" != "confirm" ]; then
    echo "Nothing has been done."
    exit -1
fi

scp $bundles $user@$server:$path/bundles/

if [ $? != 0 ]; then
    echo "Could not upload bundles."
    exit -1
fi

ssh $user@$server "${root}/helpers/generate.py -u ${url} -p ${path}/bundles/ > ${path}/index.html"

if [ $? != 0 ]; then
    echo "Could not update microformat file."
    exit -1
fi

echo "Bundles successfully updated."
