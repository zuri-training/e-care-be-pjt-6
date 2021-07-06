from time import sleep
from celery.decorators import task
from celery.utils.log import get_task_logger
from .utils import send_mail_to



logger = get_task_logger(__name__)

@task(name='my_task')
# my_first_task.delay(15)

def my_first_task(request, duration):

    error_message = ""
    is_task_completed= False

    try:
        sleep(duration)
        is_task_completed= True
    except Exception as err:
        error_message= str(err)
        logger.error(error_message)

    if is_task_completed:
        send_mail_to(request)
    else:
        return (0)
    return ("task done")
