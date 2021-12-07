from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import json
from authentication.models import School


def jobStatus(request):
    grade = School.objects.values('Grade').distinct()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT `Major` AS `Ngành`, COUNT(IF(`JobStatus` = "Đã có việc làm", "Đã có việc làm", NULL)) AS `Đã có việc làm`, COUNT(IF(`JobStatus` = "Chưa có việc làm", "Chưa có việc làm", NULL)) AS `Chưa có việc làm`, COUNT(IF(`JobStatus` = "Tiếp tục học", "Tiếp tục học", NULL)) AS `Tiếp tục học` FROM `authentication_job` GROUP BY `Major`')
    jobs = [['Ngành', 'Đã có việc làm', 'Chưa có việc làm', 'Tiếp tục học']]
    for x in cursor:
        Major = str(x[0])
        Employed = int(x[1])
        Unemployed = int(x[2])
        Studying = int(x[3])
        inner = [Major, Employed, Unemployed, Studying]
        jobs.append(inner)
    diangojob = json.dumps(jobs)
    # print(jobs)
    return render(request, 'jobStatus.html', {'Gradedata': grade, 'values': diangojob})


def jobStatus_k(request):
    grade = School.objects.values('Grade').distinct()
    if request.method == 'POST':
        result = request.POST['JobSelected']
        cursor = connection.cursor()
        cursor.execute(
            'SELECT J.`Major` AS `Ngành`, COUNT(IF(J.`JobStatus`="Đã có việc làm", "Đã có việc làm", NULL)) AS `Employed`, COUNT(IF(J.`JobStatus`="Chưa có việc làm", "Chưa có việc làm", NULL)) AS `Unemployed`, COUNT(IF(J.`JobStatus`="Tiếp tục học", "Tiếp tục học", NULL)) AS `Studying` FROM `authentication_job` AS J, `authentication_school` AS G WHERE G.`Grade`=%s AND J.`MSSV`=G.`MSSV` GROUP BY J.`Major`', [result])
        jobs = [['Ngành', 'Đã có việc làm', 'Chưa có việc làm', 'Tiếp tục học']]
        for x in cursor:
            Major = str(x[0])
            Employed = int(x[1])
            Unemployed = int(x[2])
            Studying = int(x[3])
            inner = [Major, Employed, Unemployed, Studying]
            jobs.append(inner)
        diangojob = json.dumps(jobs)
        # print(jobs)
        return render(request, 'jobStatus_k.html', {'Gradedata': grade, 'values': diangojob, 'result': result})


def otherStatistics(request):
    grade = School.objects.values('Grade').distinct()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT `JobAddress`, COUNT(`MSSV`) AS `Số lượng` FROM `authentication_address` GROUP BY `JobAddress`')
    adds = [['JobAddress', 'Số lượng']]
    for x in cursor:
        JobAddress = str(x[0])
        Counting = int(x[1])
        inner = [JobAddress, Counting]
        adds.append(inner)
    diango_a = json.dumps(adds)
    # print(diango_a)

    cursor_w = connection.cursor()
    cursor_w.execute(
        'SELECT `JobAddressWorld` AS `Việc làm`, COUNT(`MSSV`) AS `Số lượng` FROM `authentication_address` GROUP BY `JobAddressWorld`')
    addw = [['Việc làm', 'Số lượng']]
    for x in cursor_w:
        JobAddressWorld = str(x[0])
        Counting_w = int(x[1])
        inner_W = [JobAddressWorld, Counting_w]
        addw.append(inner_W)
    diango_w = json.dumps(addw)
    # print(diango_w)

    cursor_f = connection.cursor()
    cursor_f.execute(
        'SELECT `Feature`, COUNT(`MSSV`) AS `Số lượng` FROM `authentication_job` GROUP BY `Feature` ORDER BY `Số lượng` ASC')
    feature = [['Feature', 'Số lượng']]
    for x in cursor_f:
        Feature = str(x[0])
        Counting_f = int(x[1])
        inner_f = [Feature, Counting_f]
        feature.append(inner_f)
    diango_f = json.dumps(feature)
    # print(diango_f)

    return render(request, 'otherStatistics.html', {'Gradedata': grade, 'values': diango_a, 'values_w': diango_w, 'values_f': diango_f})


def otherStatistics_k(request):
    grade = School.objects.values('Grade').distinct()
    if request.method == 'POST':
        result = request.POST['OtherSelected']
        cursor = connection.cursor()
        cursor.execute(
            'SELECT J.`JobAddress`, COUNT(J.`MSSV`) AS `Số lượng` FROM `authentication_job` AS J, `authentication_school` AS S WHERE S.`Grade`=%s AND J.`MSSV`=S.`MSSV` GROUP BY J.`JobAddress`', [result])
        adds = [['JobAddress', 'Số lượng']]
        for x in cursor:
            JobAddress = str(x[0])
            Counting = int(x[1])
            inner = [JobAddress, Counting]
            adds.append(inner)
        diango_a = json.dumps(adds)
        # print(diango_a)

        cursor_w = connection.cursor()
        cursor_w.execute(
            'SELECT D.`JobAddressWorld`, COUNT(D.`MSSV`) AS `Số lượng` FROM `authentication_address` AS D, `authentication_school` AS S WHERE S.`Grade`=%s AND D.`MSSV`=S.`MSSV` GROUP BY D.`JobAddressWorld`', [result])
        addw = [['Việc làm', 'Số lượng']]
        for x in cursor_w:
            JobAddressWorld = str(x[0])
            Counting_w = int(x[1])
            inner_W = [JobAddressWorld, Counting_w]
            addw.append(inner_W)
        diango_w = json.dumps(addw)
        # print(diango_w)

        cursor_f = connection.cursor()
        cursor_f.execute(
            'SELECT J.`Feature`, COUNT(J.`MSSV`) AS `Số lượng` FROM `authentication_job` AS J, `authentication_school` AS S WHERE S.`Grade`=%s AND J.`MSSV`=S.`MSSV` GROUP BY J.`Feature`', [result])
        feature = [['Feature', 'Số lượng']]
        for x in cursor_f:
            Feature = str(x[0])
            Counting_f = int(x[1])
            inner_f = [Feature, Counting_f]
            feature.append(inner_f)
        diango_f = json.dumps(feature)
        # print(diango_f)

    return render(request, 'otherStatistics_k.html', {'Gradedata': grade, 'values': diango_a, 'values_w': diango_w, 'values_f': diango_f, 'result': result})


def income_k(request):
    grade = School.objects.values('Grade').distinct()
    if request.method == 'POST':
        result = request.POST['GradeSelected']
        cursor = connection.cursor()
        cursor.execute(
            'SELECT S.`Salary`, COUNT(S.`MSSV`) AS `Counting` FROM `authentication_salary` AS S, `authentication_school` AS G WHERE G.`Grade`=%s and S.`MSSV`=G.`MSSV` GROUP BY S.`Salary`', [result])
        income_k = [['Salary', 'Counting']]
        for x in cursor:
            Salary = str(x[0])
            Counting = int(x[1])
            inner = [Salary, Counting]
            income_k.append(inner)
        diango = json.dumps(income_k)
        # print(diango)
        return render(request, 'income_k.html', {'Gradedata': grade, 'values': diango, 'result': result})


def income(request):
    grade = School.objects.values('Grade').distinct()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT `Salary`, COUNT(`MSSV`) AS `Counting` FROM `authentication_salary` GROUP BY `Salary`')
    income = [['Salary', 'Counting']]
    for x in cursor:
        Salary = str(x[0])
        Counting = int(x[1])
        inner = [Salary, Counting]
        income.append(inner)
    diango = json.dumps(income)
    # print(diango)
    return render(request, 'income.html', {'Gradedata': grade, 'values': diango})
