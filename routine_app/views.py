# SAMIP REGMI
# SEP 1

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from sql_db.models import Routine , RoutineEntry, Section
from datetime import datetime
import pdfplumber

class RoutineView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request): 
        if not request.user.is_staff:
            messages.error(request, 'ACCESS DENIED: ADMIN ONLY')
            return redirect('index')
        
        routines = Routine.objects.all().order_by('-created_at')
        return_context = {
            'routines': routines
        }
        return render(request, 'admin/routine/create.html', context=return_context)

    def post(self, request):
        routine_pdf = request.FILES.get('routine_pdf')
        print("Received file:", routine_pdf)
        print("Content type:", getattr(routine_pdf, 'content_type', None))
        print("Size:", getattr(routine_pdf, 'size', None))

        title = request.POST.get('title', 'Routine')
        description = request.POST.get('description', '')
        show_on_website = request.POST.get('show_on_website','True')
        if not routine_pdf:
            messages.error(request, 'PLEASE UPLOAD A ROUTINE PDF.')
            return redirect('index')
        if routine_pdf.content_type != 'application/pdf':
            messages.error(request, 'ONLY PDF FILES ARE ALLOWED.')
            return redirect('index')
        
        routine = Routine.objects.create(
                            title=title,
                            description=description,
                            show_on_website=(show_on_website == 'True')
                        )


        with pdfplumber.open(routine_pdf) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                print("TABLE:", table)
                if not table:
                    continue
                # MATHI NACHAINE TITLE , ANI STREAM , INTAKE
                # START FROM 4TH ROW
                for row in table[3:]:
                    try:
                        day, time_range, class_type, module_code, subject, teacher, section_str, room = row

                        entry = RoutineEntry.objects.create(
                            routine=routine,
                            day=(day or "").strip(),
                            time_range=(time_range or "").strip(),
                            class_type=(class_type or "").strip(),
                            module_code=(module_code or "").strip(),
                            subject=(subject or "").strip(),
                            teacher=(teacher or "").strip(),
                            room=(room or "").strip()
                        )

                        if section_str:
                            for sec in section_str.split("+"):
                                sec = sec.strip()
                                if sec:
                                    section_obj, _ = Section.objects.get_or_create(name=sec)
                                    entry.sections.add(section_obj)

                    except Exception as e:
                        print(f"ERROR processing row {row}: {e}")



        messages.success(request, "ROUTINE PARSING SUCCESS")
        return redirect("index")
        