from pybars import Compiler
from lml.plugin import PluginInfo

from moban_handlebars.constants import HELPER_EXTENSION, PARTIALS_EXTENSION


class Helper(PluginInfo):
    """
    @Helper('tag_used_inside_handlebar')
    def the_actual_implementation(this, options, items):
        ...
    """
    def __init__(self, helper):
        super(Helper, self).__init__(HELPER_EXTENSION)
        self.helper = helper

    def tags(self):
        yield self.helper


def register_partial(identifier, partial):
    plugin = PluginInfo(PARTIALS_EXTENSION, tags=[identifier])
    partial = Compiler().compile(partial)
    plugin({identifier: partial})
