# Django-plop

Django-plop is a middleware for profiling your views with [PLOP][plop], the
Python Low Overhead Profiler.

## Usage

In your project settings:

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('django-plop.middleware.PlopMiddleware',)

    PLOP_DIR = os.path.join(PROJECT_ROOT, 'plop') # will be created, defaults to /tmp/plop

Then start your server with `python manage.py --noreload` (the `--noreload` is
very important.) Hit a few pages, and then start the plop viewer like so:

    python -m plop.viewer --datadir=plop

And navigate to [localhost:8888](http://localhost:8888) to view the profile
results.

### Note

`--noreload` is used in development to allow the signalling features PLOP uses.
This means it sadly won't work with some alternate runserver implementations
such as `django-devserver`. It will, however, work in prefork environments like
Gunicorn.

## Production Usage

PLOP itself is [used in production by Dropbox][dropbox-plop] with 2% CPU
overhead (or so). However, this middleware will write logs to the disk, which
may not be acceptable for your use case (especially on Heroku and other PaaSes)

## Non-goals

Django-plop won't install tornado for you (you need it to use the plop
visualizer.) This is because you can use it in production, and you may not want
to have tornado kicking around in your production environment.

[plop]: https://github.com/bdarnell/plop "plop on GitHub"
[dropbox-plop]: http://tech.dropbox.com/?p=272 "Dropbox Plop: Low-overhead profiling for Python"
