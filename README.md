# Django-plop

Django-plop is a middleware for profiling your views with [PLOP][plop], the
Python Low Overhead Profiler.

## Usage

In your project settings:

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ['django-plop.middleware.PlopMiddleware']

    PLOP_DIR = os.path.join(PROJECT_ROOT, 'plop') # will be created, defaults to /tmp/plop

## Production Usage

PLOP itself is [used in production by Dropbox][dropbox-plop] with 2% CPU
overhead (or so). However, this middleware will write logs to the disk, which
may not be acceptable for your use case (especially on Heroku et. al.)

[plop]: https://github.com/bdarnell/plop "plop on GitHub"
[dropbox-plop]: http://tech.dropbox.com/?p=272 "Dropbox Plop: Low-overhead profiling for Python"
