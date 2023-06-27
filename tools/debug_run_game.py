import logging
from mpf.core.config_loader import YamlMultifileConfigLoader

from mpf.core.machine import MachineController

config_loader = YamlMultifileConfigLoader('./', ["config.yaml"], False, False)
config = config_loader.load_mpf_config()

options = {
    'force_platform': 'smart_virtual',
    'production': False,
    'mpfconfigfile': ["mpfconfig.yaml"],
    'configfile': ["config.yaml"],
    'debug': True,
    'bcp': True,
    'no_load_cache': False,
    'create_config_cache': True,
    'text_ui': False,
    'consoleloglevel': logging.DEBUG,
}
logging.basicConfig(level=logging.DEBUG)
machine = MachineController(options, config)
machine.run()
