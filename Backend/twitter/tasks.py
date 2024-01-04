from celery import shared_task 





@shared_task
def loggering():
    print(f"\nhhhhhhhhh\n")
    return 