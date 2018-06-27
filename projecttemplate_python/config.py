"""Configuration for ProjectTemplate
"""
from pathlib import Path
from ruamel.yaml import YAML
import appdirs

_APPNAME = 'projecttemplate_python'
_APPAUTHOR = 'ProjectTemplate'

APPLICATION_DIRS = appdirs.AppDirs(appname=_APPNAME,
                                   appauthor=_APPAUTHOR,
                                   roaming=True)


def template_directories():
    """Return directories potentially containing templates

    [description]
    """
    pass


def application_configuration():
    create_application_configuration()
    config_file = Path(APPLICATION_DIRS.user_config_dir) / 'config.yaml'
    yaml = YAML()
    return yaml.load(config_file)


def create_application_configuration():
    config_dir = Path(APPLICATION_DIRS.user_config_dir)
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir/'config.yaml'
    if not config_file.exists():
        config = {
            'template_directory': '~/projecttemplates'
        }
        yaml = YAML()
        yaml.dump(config, config_file)
