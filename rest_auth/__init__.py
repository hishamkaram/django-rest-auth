try:
    from django.conf.urls import url  # noqa
except ImportError:
    from django.urls import re_path as url  # noqa
try:
    from django.utils.translation import ugettext_lazy as _  # noqa
except ImportError:
    from django.utils.translation import gettext_lazy as _  # noqa
try:
    from django.utils.encoding import force_text  # noqa
except ImportError:
    from django.utils.encoding import force_str as force_text  # noqa
