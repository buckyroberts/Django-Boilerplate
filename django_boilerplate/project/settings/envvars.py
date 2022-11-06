from django_boilerplate.core.utils.collections import deep_update
from django_boilerplate.core.utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips out the prefix, and adds it to globals() for easy reference

For example:
export DJANGO_BOILERPLATE_SETTING_IN_DOCKER=true (environment variable)

Could then be referenced as a global as:
IN_DOCKER (where the value would be True)
"""

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
