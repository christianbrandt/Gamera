#
#
# Copyright (C) 2001 Ichiro Fujinaga, Michael Droettboom, and Karl MacMillan
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

from gamera.plugin import *
import _morphology

class erode(PluginFunction):
  self_type = ImageType([ONEBIT, GREYSCALE, FLOAT])
erode = erode()

class dilate(PluginFunction):
  self_type = ImageType([ONEBIT, GREYSCALE, FLOAT])
dilate = dilate()

class erode_dilate(PluginFunction):
  self_type = ImageType([ONEBIT, GREYSCALE, FLOAT])
  args = Args([Int('number of times', range=(0, 10), default=1), \
               Choice('direction', ['dilate', 'erode']), \
               Choice('window shape', ['rectangular', 'octagonal'])])
erode_dilate = erode_dilate()

class rank(PluginFunction):
  self_type = ImageType([ONEBIT, GREYSCALE, FLOAT])
  args = Args([Int('rank', range=(1, 9))])
rank = rank()

class mean(PluginFunction):
  self_type = ImageType([GREYSCALE, FLOAT])
mean = mean()

class MorphologyModule(PluginModule):
  cpp_headers = ["morphology.hpp"]
  cpp_namespaces = ["Gamera"]
  category = "Morphology"
  functions = [erode_dilate, erode, dilate, rank, mean]
  author = "Michael Droettboom and Karl MacMillan"
  url = "http://gamera.dkc.jhu.edu/"

module = MorphologyModule()
