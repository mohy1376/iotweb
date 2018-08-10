from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class MyApphook(CMSApp):
    app_name = 'iot'  # must match the application namespace
    name = "My Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["iot:urls.py"] # replace this with the path to your application's URLs module
