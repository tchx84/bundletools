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


HEADER = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
<title>Micro-format File</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
<table>
'''

CONTENT = '''
<tr>
<td class="olpc-activity-info">
<span class="olpc-activity-id">%s</span>
<span class="olpc-activity-version">%s</span>
<span class="olpc-activity-url"><a href="%s">download</a></span>
</td>
</tr>
'''

FOOTER = '''
</table>
</body>
</html>
'''


def generate(url, path):
    bundles = Bundles(url, path)
    bundles.find()

    output = ''
    output += HEADER
    for bundle in sorted(bundles, key=lambda e: e['id']):
        output += CONTENT % (bundle['id'], bundle['version'], bundle['url'])
    output += FOOTER

    print output

if __name__ == "__main__":
    parser = ArgumentParser(description='generates microformat')
    parser.add_argument('-u', '--url',
                        type=str,
                        dest='url',
                        required=True)
    parser.add_argument('-p', '--path',
                        type=str,
                        dest='path',
                        required=True)

    args = parser.parse_args()
    generate(args.url, args.path)
