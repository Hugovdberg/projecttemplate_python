# -*- coding: utf-8 -*-
"""ProjectTemplate

Class to describe project templates and create projects from them
"""
from pathlib import Path


class ProjectTemplate(object):
    """ProjectTemplate

    Create and update project templates
    """

    def __init__(self, template_name):
        self.template_name = template_name

    def create_template(self, source='minimal'):
        """Create the current template from the given source

        Create a template by the given template name from an existing template.

        Args:
            source (str): Template name to create the new template from
        """
        from projecttemplate_python.config import application_configuration
        config = application_configuration()
