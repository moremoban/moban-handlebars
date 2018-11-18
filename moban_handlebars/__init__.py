# flake8: noqa
from moban_handlebars._version import __version__
from moban_handlebars._version import __author__

from lml.plugin import PluginInfo, PluginInfoChain
import moban.constants as constants


PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        constants.TEMPLATE_ENGINE_EXTENSION,
        "%s.engine.EngineHandlebars" % __name__,
        tags=["handlebars", "hbs"],
    )
)
