from lml.plugin import PluginInfo
from moban_handlebars.constants import PARTIALS_EXTENSION
from pybars import Compiler


def register_partial(identifier, partial):
    plugin = PluginInfo(PARTIALS_EXTENSION, tags=[identifier])
    partial = Compiler().compile(partial)
    plugin({identifier: partial})
