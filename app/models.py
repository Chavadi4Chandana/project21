from django.db import models

# Create your models here.
class Deptrtment(models.Model):
    dname=models.CharField(max_length=100,unique=True)
    deptno=models.IntegerField(primary_key=True)
    loc=models.CharField(max_length=100)

class Employee(models.Model):
    ename=models.CharField(max_length=100)
    empno=models.IntegerField(primary_key=True)
    sal=models.IntegerField()
    job=models.CharField(max_length=100)
    comm=models.IntegerField()
    mgr=models.IntegerField()
    hiredate=models.IntegerField()
    deptno=models.ForeignKey(Deptrtment,on_delete=models.CASCADE)

class Bonus(models.Model):
    amount=models.IntegerField()

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.IntegerField()
    hisal=models.IntegerField()










