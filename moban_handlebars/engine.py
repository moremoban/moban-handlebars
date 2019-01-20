import sys
import codecs

import moban.utils as utils
from pybars import Compiler


class EngineHandlebars(object):
    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        with codecs.open(actual_file, "r", encoding="utf-8") as source:
            hbr_template = Compiler().compile(source.read())
        return hbr_template

    def get_template_from_string(self, string):
        if sys.version_info < (3, 0):
            # Python 2 strings are not unicode by default
            string = unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content
