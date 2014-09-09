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

import re
import os
import io

from urlparse import urljoin
from zipfile import ZipFile
from ConfigParser import ConfigParser


class Bundles(list):

    def __init__(self, url, path):
        self._url = url
        self._path = path

    def normalized(self, version):
        return [int(n) for n in re.findall('\\b\\d+\\b', version)]

    def is_newer(self, version1, version2):
        if self.normalized(version1) > self.normalized(version2):
            return True
        return False

    def find(self):
        _index = {}

        for name in os.listdir(self._path):
            if not name.endswith('.xo'):
                continue

            with ZipFile(os.path.join(self._path, name), 'r') as bundle:
                for content in bundle.namelist():
                    if not content.endswith('activity/activity.info'):
                        continue

                    parser = ConfigParser()
                    parser.readfp(io.BytesIO(bundle.read(content)))

                    bundle_id = parser.get('Activity', 'bundle_id')
                    version = parser.get('Activity', 'activity_version')

                    info = _index.get(bundle_id, None)

                    if info is not None:
                        if self.is_newer(version, info['version']):
                            self.remove(info)
                        else:
                            continue

                    name = parser.get('Activity', 'name')
                    url = urljoin(self._url, os.path.join('./bundles', name))

                    info = {'id': bundle_id,
                            'version': version,
                            'name': name,
                            'url': url}

                    self.append(info)
                    _index[bundle_id] = info
                    break
