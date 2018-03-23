from django.shortcuts import render,redirect
from student.models import *

from office.models import *
from hod.models import *
import random

# Create your views here.

def office_active(request): 
    print request.user
    temp_office=Office.objects.filter(status="")
    if request.method=='POST':
        temp_id=request.POST['id']
        temp_remarks=request.POST['remarks']
        temp_status=request.POST['status']
	#temp_id=request.user
        office=Office.objects.filter(id_number=temp_id)[0]
        office.status=temp_status
        office.remarks=temp_remarks
        office.save()
        if temp_status == "yes":
            hod=HOD()
            hod.id_number=office.id_number
            hod.department=office.department
            hod.certificate_type=office.certificate_type
            hod.status=""
            hod.remarks=""
            hod.save()

    return render(request,'office/active.html',{'office':temp_office,'department':"office"})

def office_pending(request): 
    print request.user
    temp_office=Office.objects.filter(status="no")
    if request.method=='POST':
        temp_id=request.POST['id']
        temp_remarks=request.POST['remarks']
        temp_status=request.POST['status']
	#temp_id=request.user
        office=Office.objects.filter(id_number=temp_id)[0]
        office.status=temp_status
        office.remarks=temp_remarks
        office.save()
        if temp_status == "yes":
            hod=HOD()
            hod.id_number=office.id_number
            hod.department=office.department
            hod.certificate_type=office.certificate_type
            hod.status=""
            hod.remarks=""
            hod.save()
    return render(request,'office/pending.html',{'office':temp_office,'department':"office"})

def office_approved(request): 
    print request.user
    temp_office=Office.objects.filter(status="yes")
    return render(request,'office/approved.html',{'office':temp_office,'department':"office"})

def office_issue_approved(request): 
    temp_office=Office_final.objects.filter(final_status="yes")
    return render(request,'office/approved_issue.html',{'office':temp_office,'department':"office"})

def office_ack_1(request): 
    return render(request,'office/ack_1.html',{'department':"office"})


def office_issue(request): 
    temp_office=Office_final.objects.filter(final_status="")
    return render(request,'office/all_issue.html',{'office':temp_office,'department':"office"})

def office_issue_id(request,student_id): 
    temp_office=Office_final.objects.filter(id_number=student_id)[0]
    if request.method == 'POST':
        new_file_name = 'data/certificates/' + str(student_id) + "_PC_" + str(random.randrange(1,1000)) 
        filename = move_file(request.FILES['pc_file'], new_file_name)#SupervisorChange Approval uploaded file
        temp_office.pc = new_file(filename) #Storing file in the specified location as new_file_name
        new_file_name = 'data/certificates/' + str(student_id) + "_MarksMemo_" + str(random.randrange(1,1000)) 
        filename = move_file(request.FILES['marksmemo_file'], new_file_name)#SupervisorChange Approval uploaded file
        temp_office.marks_memos = new_file(filename) #Storing file in the specified location as new_file_name
        new_file_name = 'data/certificates/' + str(student_id) + "_Study_" + str(random.randrange(1,1000)) 
        filename = move_file(request.FILES['study_file'], new_file_name)#SupervisorChange Approval uploaded file
        temp_office.study = new_file(filename) #Storing file in the specified location as new_file_name
        temp_office.final_status="yes"
        temp_office.save()
        return redirect('/office/ack1')
    return render(request,'office/issue.html',{'office':temp_office,'department':"office"})


def new_file(file_path):  #Storing the file in db 
    files  = File.objects.filter(path = file_path)
    if len(files) < 1:
        file_o = File()  #Creating a file tuple
        file_o.name = file_path.split('/')[-1]   #Storing file name 
        file_o.path = file_path 
        file_o.save()
    else:
        file_o = files[0]
    return file_o

def move_file(f, filename):  #Storing a file in the specified location 
    extension = f.name.split(".")[-1]   
  #Writing the data into a location
    with open(filename + "." + extension, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename + "." + extension

