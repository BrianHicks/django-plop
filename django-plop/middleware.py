'plop middleware'
from django.conf import settings
from plop.collector import Collector
import os

try:
    PLOP_DIR = settings.PLOP_DIR
except AttributeError:
    PLOP_DIR = os.environ.get('PLOP_DIR', '/tmp/plop')


class PlopMiddleware(object):
    'middleware to profile views with plop'
    def __init__(self):
        'make sure PLOP_DIR exists'
        if not os.path.exists(PLOP_DIR):
            os.mkdir(PLOP_DIR)

    def get_filename(self, func):
        'get the filename for a function'
        return os.path.join(PLOP_DIR, func.__name__)

    def process_view(self, request, view_func, _, __):
        'process a single view, adding the collector'
        request.collector = Collector()
        request.collector.start()
        request.plop_filename = self.get_filename(view_func)

    def process_response(self, request, response):
        'after the view executes, stop profiling'
        if hasattr(request, 'collector'): # 404s
            request.collector.stop()
            with open(request.plop_filename, 'a') as plop_file:
                plop_file.write(repr(dict(request.collector.stack_counts)))

        return response

    def process_exception(self, request, exception):
        'process an exception - just stop profiling'
        request.collector.stop()
