from django.http import JsonResponse
from django.views import View
from sql_db.models import Routine

class RoutineUserAPIView(View):
    def get(self, request):
        day = request.GET.get('day') 
        section = request.GET.get('section') 

        if not day or not section:
            return JsonResponse({'error': 'BOTH DAY AND SECTION IS REQUIRED'}, status=400)

        routines = Routine.objects.filter(show_on_website=True)
        routines_list = []

        for routine in routines:
            entries = routine.entries.filter(day=day, sections__name=section).distinct().order_by('time_range')

            entries_data = []
            for entry in entries:
                entries_data.append({
                    'time_range': entry.time_range,
                    'class_type': entry.class_type,
                    'module_code': entry.module_code,
                    'subject': entry.subject,
                    'sections': [s.name for s in entry.sections.all()],
                    'teacher': entry.teacher,
                    'room': entry.room
                })

            if entries_data: 
                routines_list.append({
                    'routine_id': routine.id,
                    'routine_title': routine.title,
                    'routine_description': routine.description,
                    'entries': entries_data
                })

        return JsonResponse({'routines': routines_list})
