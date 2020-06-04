from pybars import Compiler
from moban.externals import file_system


class EngineHandlebars(object):
    ACTION_IN_PRESENT_CONTINUOUS_TENSE = "Handlebars-ing"
    ACTION_IN_PAST_TENSE = "Handlebarsed"

    def __init__(self, template_fs, options=None):
        """
        template_fs is a multfs instance and gives you the power to load
        a template from equiped template directories.

        :param fs.multifs.MultiFS template_fs: a MultiFS instance or a FS instance
        :param options: a dictionary of potential parameters.
                        not used yet.
        """
        self.template_fs = template_fs

    def get_template(self, template_file):
        template_file = file_system.to_unicode(template_file)
        content = self.template_fs.readtext(template_file)
        hbr_template = Compiler().compile(content)
        return hbr_template

    def get_template_from_string(self, string):
        string = file_system.to_unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data, _):
        rendered_content = "".join(template(data))
        rendered_content = rendered_content
        return rendered_content
