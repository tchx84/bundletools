#!/usr/bin/env python

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

from argparse import ArgumentParser

from libs.bundles import Bundles


def inventory(path):
    bundles = Bundles('http://wildcard.org/', path)
    bundles.find()

    for bundle in sorted(bundles, key=lambda e: e['id']):
        print '%s;%s' % (bundle['id'], bundle['name'])


if __name__ == "__main__":
    parser = ArgumentParser(description='outputs CVS for all bundles')
    parser.add_argument('-p', '--path',
                        type=str,
                        dest='path',
                        required=True)

    args = parser.parse_args()
    inventory(args.path)
