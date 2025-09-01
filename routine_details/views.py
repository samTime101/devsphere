# SEP 1
# SAMIP REGMI

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Case, When
from sql_db.models import Routine, RoutineEntry

class RoutineDetailView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        routines = Routine.objects.all()
        routine_data = []

        # ROUTINE KO ORDERING GARNA
        for routine in routines:
            day_ordering = Case(
                When(day='SUN', then=1),
                When(day='MON', then=2),
                When(day='TUE', then=3),
                When(day='WED', then=4),
                When(day='THU', then=5),
                When(day='FRI', then=6),
            )
            entries = RoutineEntry.objects.filter(routine=routine).annotate(
                day_order=day_ordering
            ).order_by('day_order', 'time_range')

            for entry in entries:
                entry.section_names = [section.name for section in entry.sections.all()]

            routine_data.append({
                'routine': routine,
                'entries': entries
            })

        return render(request, 'admin/routine/detail.html', context={'routine_data': routine_data})

    def post(self, request):
        routine_id = request.POST.get('routine_id')
        try:
            routine = Routine.objects.get(id=routine_id)
            routine.show_on_website = not routine.show_on_website
            routine.save()
            messages.success(request, f"'{routine.title}' UPDATED SUCCESSFULLY")
        except Routine.DoesNotExist:
            messages.error(request, "ROUTINE NOT FOUND")
        return redirect('routine_detail')

