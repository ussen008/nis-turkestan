from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from studentapp.forms import AppealForms, ParticipantForm, AddStudent
from .models import Student, AppealCurators
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import StudentFilter


def index(request):
    return render(request, 'studentapp/index.html')


def students(request):
    object_list = Student.objects.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(page.num_pages)

    myfilter = StudentFilter(request.GET, queryset=object_list)   
    return render(request, 'studentapp/students_page.html', {'students': students, 'page': page, 'myfilter': myfilter})


def student(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'studentapp/single_page.html', {'student': student})


# def by_klass(request):
#     indv_klass = Student.objects.filter(klass=Student.klass)
#     return render(request, 'studentapp/by_class.html', {'indv_klass': indv_klass})


def info(request):
    chartqueryset = Student.objects.all().count()
    print(chartqueryset)
    return render(request, 'studentapp/info.html', {'chartqueryset': chartqueryset})


def appeal_upload(request):
    if request.method == 'POST':
        form = AppealForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appeal')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = AppealForms()
    return render(request, 'studentapp/appeal.html', {'form': form})


# AJAX
def load_students(request):
    category_class_id = request.GET.get('category_class')
    students_list = Student.objects.filter(category_class_id=category_class_id)
    return render(request, 'studentapp/student_dropdown_list_options.html', {'students_list': students_list})
    print(list(students.values('id', 'full_name')))
    return JsonResponse(list(students.values('id', 'full_name')), safe=False)

def participant_upload(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = ParticipantForm()
    return render(request, 'studentapp/participant.html', {'form': form})


def add_student(request):
    if request.method == 'POST':
        student_form = AddStudent(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect('student_list')
        else:
            return HttpResponse('Form is not valid')
    else:
        student_form = AddStudent()
    return render(request, 'studentapp/add_student.html', {'student_form': student_form})
    
