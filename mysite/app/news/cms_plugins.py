
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Hello 

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = Hello
    name = _("news article")
    render_template = "news/_news_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HelloPlugin, self).render(context, instance, placeholder)
        return context
 