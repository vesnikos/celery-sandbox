from celery import Celery
from . import celeryconfig

capp = Celery("MyAwesomeCelery", include=["app.tasks", ])
# capp.config_from_object(celeryconfig, silent=False)
# capp.autodiscover_tasks( force=True)
