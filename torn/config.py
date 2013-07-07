"""
Provides a clean method for importing default settings and
user override settings.
"""

from tornado.util import ObjectDict

def load_settings(user_settings):
    """ Parse user settings, imports local settings, etc. """
    try:
        import settings_local
        user_settings.update(settings_local.settings)
    except ImportError:
        pass

    settings = ObjectDict(user_settings)
    return settings
