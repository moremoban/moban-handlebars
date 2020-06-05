from pybars import Compiler
from lml.plugin import PluginInfo

from moban_handlebars.constants import PARTIALS_EXTENSION


def register_partial(identifier, partial):
    plugin = PluginInfo(PARTIALS_EXTENSION, tags=[identifier])
    partial = Compiler().compile(partial)
    plugin({identifier: partial})
