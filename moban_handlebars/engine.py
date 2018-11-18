import codecs

import moban.utils as utils
from pybars import Compiler


class EngineHandlebars(object):
    def __init__(self, template_dirs):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        with codecs.open(actual_file, "r", encoding="utf-8") as source:
            hbr_template = Compiler().compile(source.read())
        return hbr_template

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content
