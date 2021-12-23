try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_str as force_text
