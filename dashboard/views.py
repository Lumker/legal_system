# dashboard/views.py
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from deadlines.models import Deadline
from cases.models import Case
# from billing.models import TimeEntry, Invoice
from django.db import models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def dashboard(request):
    if not request.user.has_perm('dashboard.view_dashboard'):
        raise PermissionDenied("You do not have access to the dashboard.")
    ...
    # Upcoming deadlines
    today = timezone.now().date()
    upcoming_deadlines = Deadline.objects.filter(
        date__lte=today + timedelta(days=3),
        notified=False
    ).select_related('case__client', 'case__lawyer')

    # Case status breakdown
    case_stats = Case.objects.values('status').annotate(count=models.Count('id'))

    # Billing efficiency
    # total_hours = TimeEntry.objects.aggregate(total=models.Sum('duration'))['total'] or 0
    # billed_hours = Invoice.objects.aggregate(total=models.Sum('hours_billed'))['total'] or 0
    # efficiency = (billed_hours / total_hours * 100) if total_hours else 0

    # context = {
    #     'upcoming_deadlines': upcoming_deadlines,
    #     'case_stats': case_stats,
    #     'total_hours': total_hours.total_seconds() / 3600 if total_hours else 0,
    #     'billed_hours': billed_hours.total_seconds() / 3600 if billed_hours else 0,
    #     'efficiency': efficiency,
    #     'pro_bono_cases': Case.objects.filter(is_pro_bono=True).count()
    # }
    # return render(request, 'dashboard/index.html', context)