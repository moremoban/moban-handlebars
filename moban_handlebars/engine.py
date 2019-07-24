import sys

import moban.utils as utils
from pybars import Compiler
import fs

PY2 = sys.version_info[0] == 2


class EngineHandlebars(object):
    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        content = read_file(actual_file)
        hbr_template = Compiler().compile(content)
        return hbr_template

    def get_template_from_string(self, string):
        if PY2:
            # Python 2 strings are not unicode by default
            string = to_unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content


def read_file(path):
    try:
        path = to_unicode(path)
        dir_name = fs.path.dirname(path)
        the_file_name = fs.path.basename(path)
        with fs.open_fs(dir_name) as fs_system:
            with fs_system.open(the_file_name) as file_handle:
                return file_handle.read()
    except:
        print(path)
        raise


def to_unicode(path):
    if PY2:
        if isinstance(path, unicode) is False:
            return unicode(path)
    return path
