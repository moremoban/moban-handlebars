from typing import Dict

from pybars import Compiler
from lml.plugin import PluginManager
from moban.externals import file_system

from moban_handlebars.constants import HELPER_EXTENSION, PARTIALS_EXTENSION


class HandlebarsHelperManager(PluginManager):
    def __init__(self):
        super(HandlebarsHelperManager, self).__init__(HELPER_EXTENSION)

    def get_all(self):
        for name in self.registry.keys():
            the_helper = self.load_me_now(name)
            yield (name, the_helper)


class HandlebarsPartialManager(PluginManager):
    def __init__(self):
        super(HandlebarsPartialManager, self).__init__(PARTIALS_EXTENSION)

    def get_all(self):
        for name in self.registry.keys():
            partial = self.load_me_now(name)
            yield (name, partial[name])


HELPERS = HandlebarsHelperManager()
PARTIALS = HandlebarsPartialManager()


class EngineHandlebars(object):
    ACTION_IN_PRESENT_CONTINUOUS_TENSE = "Handlebars-ing"
    ACTION_IN_PAST_TENSE = "Handlebarsed"

    def __init__(self, template_fs, options: Dict = None):
        """
        template_fs is a multfs instance and gives you the power to load
        a template from equiped template directories.

        :param fs.multifs.MultiFS template_fs: a MultiFS/FS instance
        :param options: a dictionary of potential parameters.
                        not used yet.
        """
        self.template_fs = template_fs

    def get_template(self, template_file: str):
        template_file = file_system.to_unicode(template_file)
        content = self.template_fs.readtext(template_file)
        hbr_template = Compiler().compile(content)
        return hbr_template

    def get_template_from_string(self, string: str):
        string = file_system.to_unicode(string)
        return Compiler().compile(string)

    def apply_template(self, template, data: Dict, _):
        helpers = HELPERS.get_all()
        helpers = dict(list(helpers))

        partials = PARTIALS.get_all()
        partials = dict(list(partials))
        rendered_content = "".join(
            template(data, helpers=helpers, partials=partials)
        )
        rendered_content = rendered_content
        return rendered_content
