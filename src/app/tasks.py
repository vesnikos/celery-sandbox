from app.celery import capp


@capp.task
def echo(string: str) -> str:
    print(string)

    return string
