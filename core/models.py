from django.db import models
from django.forms import CharField, TextInput
from django.core.validators import MinValueValidator, MaxValueValidator





# Create your models here.

class Quiz(models.Model):
    question_one = models.TextField(blank=True,null=True,default=None)
    optA_question_one = models.CharField(max_length=50, default=None)
    optB_question_one = models.CharField(max_length=50, default=None)
    optC_question_one = models.CharField(max_length=50, default=None)
    question_one_c = models.IntegerField(default=0, blank=True, null=True)
    question_two = models.TextField(default=None, null=True, blank=True)
    optA_question_two = models.CharField(max_length=50, default=None)
    optB_question_two = models.CharField(max_length=50, default=None)
    optC_question_two = models.CharField(max_length=50, default=None)
    question_two_c = models.IntegerField(default=0, blank=True, null=True)
    question_three = models.TextField(default=None, null=True, blank=True)
    optA_question_three = models.CharField(max_length=50, default=None)
    optB_question_three = models.CharField(max_length=50, default=None)
    optC_question_three = models.CharField(max_length=50, default=None)
    question_three_c = models.IntegerField(default=0, blank=True, null=True)
    question_four = models.TextField(default=None, null=True, blank=True)
    optA_question_four = models.CharField(max_length=50, default=None)
    optB_question_four = models.CharField(max_length=50, default=None)
    optC_question_four = models.CharField(max_length=50, default=None)
    question_four_c = models.IntegerField(default=0, blank=True, null=True)
    question_five = models.TextField(default=None, blank=True, null=True)
    optA_question_five = models.CharField(max_length=50, default=None)
    optB_question_five = models.CharField(max_length=50, default=None)
    optC_question_five = models.CharField(max_length=50, default=None)
    question_five_c = models.IntegerField(default=0, blank=True, null=True)
    question_six = models.TextField(default=None, blank=True, null=True)
    optA_question_six = models.CharField(max_length=50, default=None)
    optB_question_six = models.CharField(max_length=50, default=None)
    optC_question_six = models.CharField(max_length=50, default=None)
    question_six_c = models.IntegerField(default=0, blank=True, null=True)
    question_seven = models.TextField(default=None, blank=True, null=True)
    optA_question_seven = models.CharField(max_length=50, default=None)
    optB_question_seven = models.CharField(max_length=50, default=None)
    optC_question_seven = models.CharField(max_length=50, default=None)
    question_seven_c = models.IntegerField(default=0, blank=True, null=True)
    question_eight = models.TextField(default=None, blank=True, null=True)
    optA_question_eight = models.CharField(max_length=50, default=None)
    optB_question_eight = models.CharField(max_length=50, default=None)
    optC_question_eight = models.CharField(max_length=50, default=None)
    question_eight_c = models.IntegerField(default=0, blank=True, null=True)
    question_nine = models.TextField(default=None, blank=True, null=True)
    optA_question_nine = models.CharField(max_length=50, default=None)
    optB_question_nine = models.CharField(max_length=50, default=None)
    optC_question_nine = models.CharField(max_length=50, default=None)
    question_nine_c = models.IntegerField(default=0, blank=True, null=True)
    question_ten = models.TextField(default=None, blank=True, null=True)
    optA_question_ten = models.CharField(max_length=50, default=None)
    optB_question_ten = models.CharField(max_length=50, default=None)
    optC_question_ten = models.CharField(max_length=50, default=None)
    question_ten_c = models.IntegerField(default=0, blank=True, null=True)
    fastwinner = models.CharField(max_length=50, default=0, blank=True)

class UserAnswer(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=15, blank=True,null=True,default=None)
    name = models.CharField(max_length=225, null=True, blank=True )
    verified = models.BooleanField(default=False,blank=True)
    answer_one = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_oneC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerOne_status = models.BooleanField(default=False, blank=True)
    answer_two = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_twoC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answertwo_status = models.BooleanField(default=False, blank=True)
    answer_three = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_threeC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerThree_status = models.BooleanField(default=False, blank=True)
    answer_four = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_fourC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerFour_status = models.BooleanField(default=False, blank=True)
    answer_five = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_fiveC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerFive_status = models.BooleanField(default=False, blank=True)
    answer_six = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_sixC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerSix_status = models.BooleanField(default=False, blank=True)
    answer_seven = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_sevenC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerSeven_status = models.BooleanField(default=False, blank=True)
    answer_eight = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_eightC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerEight_status = models.BooleanField(default=False, blank=True)
    answer_nine = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_nineC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerNine_status = models.BooleanField(default=False, blank=True)
    answer_ten = models.CharField(max_length=50, default=None, blank=True,null=True)
    answer_tenC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)], default=0)
    answerTen_status = models.BooleanField(default=False, blank=True)
    total = models.IntegerField(default=0)
    fastwinner =models.BooleanField(default=False, blank=True)
    
    winnername = models.CharField(max_length=50, default=None, blank=True,null=True)
    winnernumber =  models.CharField(max_length=11, default=None, blank=True,null=True)
    winneraccount = models.CharField(max_length=10, default=None, blank=True, null=True)
    Bank_name = models.CharField(max_length=50, default=None, blank=True,null=True)


    def user_id(self):
        return self.user_id

    def totalsec(self):
        dy = self.answer_oneC + self.answer_twoC + self.answer_threeC + self.answer_fourC + self.answer_fiveC + self.answer_sixC + self.answer_sevenC + self.answer_eightC + self.answer_nineC + self.answer_tenC
        return dy


    
    
    
    
    
    
    
    
    
    




