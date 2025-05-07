# deadlines/tasks.py
import logging
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Deadline

logger = logging.getLogger(__name__)

@shared_task
def check_deadlines():
    today = timezone.now().date()
    logger.info(f"Today: {today}")
    
    upcoming_deadlines = Deadline.objects.filter(
        date__lte=today + timedelta(days=3),
        notified=False
    )
    logger.info(f"Found {upcoming_deadlines.count()} deadlines")
    
    for deadline in upcoming_deadlines:
        logger.info(f"Processing deadline ID {deadline.id}")
        # Your existing email logic here
        deadline.notified = True
        deadline.save()
        logger.info(f"Marked deadline {deadline.id} as notified")