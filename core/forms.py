from dataclasses import fields
from django.forms import ModelForm


from .models import Quiz, UserAnswer


class UploadForm(ModelForm):
    
    class Meta:
        model = Quiz
        fields = [
        'question_one',
        'question_two',
        'question_three',
        'question_four',
        'question_five',
        'question_six',
        'question_seven',
        'question_eight',
        'question_nine',
        'question_ten',
        'optA_question_one','optB_question_one', 'optC_question_one','question_one_c',
        'optA_question_two','optB_question_two', 'optC_question_two','question_two_c',
        'optA_question_three','optB_question_three', 'optC_question_three','question_three_c',
        'optA_question_four','optB_question_four', 'optC_question_four','question_four_c',
        'optA_question_five','optB_question_five', 'optC_question_five','question_five_c',
        'optA_question_six','optB_question_six', 'optC_question_six','question_six_c',
        'optA_question_seven','optB_question_seven', 'optC_question_seven','question_seven_c',
        'optA_question_eight','optB_question_eight', 'optC_question_eight','question_eight_c',
        'optA_question_nine','optB_question_nine', 'optC_question_nine','question_nine_c',
        'optA_question_ten','optB_question_ten', 'optC_question_ten','question_ten_c',

         ]

class UploadUserAnswer(ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['id','name', 'user','verified','winnername','winnernumber', 'winneraccount','Bank_name']