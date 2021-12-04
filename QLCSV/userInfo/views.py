from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import Student, School, Job, GPA, Account


def editProfile(request):
    user = Account.objects.get(Username=request.session['username'])
    if request.method == 'POST':

        # Update value in 'Student' table
        user.FirstName = request.POST.get('FirstName')
        user.LastName = request.POST.get('LastName')
        user.Email = request.POST.get('Email')

        # Update user avatar
        if request.FILES.get('avatar', False):  # Check if user updated image
            user.profile.image = request.FILES['avatar']

        # If user is a student
        if user.Group.name == 'student':
            editStudent = Student.objects.get(MSSV=request.session['username'])
            editSchool = School.objects.get(MSSV=request.session['username'])
            editJob = Job.objects.get(MSSV=request.session['username'])
            editStudent.DateOfBirth = request.POST.get('DateOfBirth')
            editStudent.PhoneNumber = request.POST.get('PhoneNumber')
            editStudent.Gender = request.POST.get('Gender')
            editStudent.Address = request.POST.get('Address')

            # Update value in 'School' table
            editSchool.Achievement = request.POST.get('Achievement')

            # Update value in 'Job' table
            editJob.JobStatus = request.POST.get('JobStatus')
            editJob.JobName = request.POST.get('JobName')
            editJob.JobAddress = request.POST.get('JobAddress')
            editJob.TimeToStart = request.POST.get('TimeToStart')

            editStudent.save()
            editSchool.save()
            editJob.save()
        user.profile.save()
        user.save()
        return redirect(f'/userInfo/profile/{user.Username}')
    return render(request, 'userInfoEdit.html')


@login_required
def profile(request, user_mssv):
    user = Account.objects.get(Username=user_mssv)
    if user.Group.name == 'student':
        userSchool = School.objects.get(MSSV=user_mssv)
        userJob = Job.objects.get(MSSV=user_mssv)
        return render(request, 'userInfo.html', {"user": user, "userSchool": userSchool, "userJob": userJob})
    return render(request, 'userInfo.html', {"user": user})
