import sys

from moban import utils, file_system
from pybars import Compiler

PY2 = sys.version_info[0] == 2


class EngineHandlebars(object):
    def __init__(self, template_dirs, options=None):
        """
        :param template_dirs: a list of template dirs
        :param options: a dictionary of potential parameters.
                        not used yet.
        """
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        content = file_system.read_unicode(actual_file)
        hbr_template = Compiler().compile(content)
        return hbr_template

    def get_template_from_string(self, string):
        string = file_system.to_unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content
