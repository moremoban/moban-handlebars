import sys

from moban import utils, file_system
from pybars import Compiler

PY2 = sys.version_info[0] == 2


class EngineHandlebars(object):
    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        content = file_system.read_unicode(actual_file)
        hbr_template = Compiler().compile(content)
        return hbr_template

    def get_template_from_string(self, string):
        if PY2:
            # Python 2 strings are not unicode by default
            string = unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content
