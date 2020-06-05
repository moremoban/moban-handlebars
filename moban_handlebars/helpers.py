from lml.plugin import PluginInfo

from moban_handlebars.constants import HELPER_EXTENSION


class HandlebarHelper(PluginInfo):
    def __init__(self, helper):
        super(HandlebarHelper, self).__init__(HELPER_EXTENSION)
        self.helper = helper

    def tags(self):
        yield self.helper
