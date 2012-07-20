# Django-plop

Django-plop is a middleware for profiling your views with [PLOP][plop], the
Python Low Overhead Profiler.

## Usage

In your project settings:

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ['django-plop.middleware.PlopMiddleware']

    PLOP_DIR = os.path.join(PROJECT_ROOT, 'plop') # will be created, defaults to /tmp/plop

[plop]: https://github.com/bdarnell/plop "plop on GitHub"
