

from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.forms import UploadForm, UploadUserAnswer
from . models import Quiz, UserAnswer



def index(request):     

    if request.method == 'POST':
        form = UploadUserAnswer(request.POST)      
        if form.is_valid():
            form.save()
            user_id = form.save(id)
            user_id = user_id.id
            # print(user_id)
            Reg_user = (form.cleaned_data['user'])
            # print(Reg_user)
            list = ('+2347016803709','+2348136605455','075')
            if Reg_user in list:
                verify = form.save(commit=False)
                verify.verified = True
                form.save()
                return redirect('role', user_id)
            elif Reg_user not in list:
                return redirect('fail2')
                
    else:
        form = UploadUserAnswer()
    context = {
        'form': form
    }
    
    return render (request, 'index.html', context)

    
def role(request, user_id):
    print(user_id)
    user = UserAnswer.objects.get(pk=user_id)
    print(user)      
    if user.verified == True:
        return redirect('question', user_id)
    else:
        return render (request, 'fail.html')
    
    context={
        'user':user
    }
        
    return render(request, user_id)

def fail_auth(request):
    return render(request, 'fail.html')

def fail2(request):
    return render(request, 'fail2.html')
# def index(request):     

#     if request.method == 'POST':
#         form = UploadUserAnswer(request.POST)      
#         if form.is_valid():
#             form.save()
#             user_id = form.save(id)
#             user_id = user_id.id
#             # print(user_id)
#             Reg_user = (form.cleaned_data['user'])
#             # print(Reg_user)
#             list = ['+2347016803709','+2348136605455','075']
#             for lists in list:
#                 if Reg_user == lists:
#                     verify = form.save(commit=False)
#                     verify.verified = True
#                     form.save()
#                     return redirect('role', user_id)
#                 elif Reg_user != list:
#                     return redirect('fail2')
#                     print('faggg')
#                 else:
#                     print('dummmmmmy')
                
#     else:
#         form = UploadUserAnswer()
#     context = {
#         'form': form
#     }
    
#     return render (request, 'index.html', context)


def question(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerOne_status == True:
        return redirect('question2', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerOne_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_oneC += 1
                user_answer.answer_one = quiz.optA_question_one
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_one = quiz.optB_question_one
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_one = quiz.optC_question_one
                user_answer.save()
            return redirect('question2', user_id)
            
    # user_answer.answerOne_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question.html', context)



def question2(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answertwo_status == True:
        return redirect('question3', user_id)
    else:
        if request.method == 'POST':
            user_answer.answertwo_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_twoC += 1
                user_answer.answer_two = quiz.optA_question_two
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_two = quiz.optB_question_two
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_two = quiz.optC_question_two
                user_answer.save()
            return redirect('question3', user_id)
            
    # user_answer.answertwo_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question2.html', context)


def question3(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerThree_status == True:
        return redirect('question4', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerThree_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_threeC += 1
                user_answer.answer_three = quiz.optA_question_three
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_three = quiz.optB_question_three
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_three = quiz.optC_question_three
                user_answer.save()
            return redirect('question4', user_id)
            
    # user_answer.answerThree_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question3.html', context)


def question4(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerFour_status == True:
        return redirect('question5', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerFour_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_fourC += 1
                user_answer.answer_four = quiz.optA_question_four
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_four = quiz.optB_question_four
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_four = quiz.optC_question_four
                user_answer.save()
            return redirect('question5', user_id) 
            
    # user_answer.answerFour_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question4.html', context)


def question5(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerFive_status == True:
        return redirect('question6', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerFive_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_fiveC += 1
                user_answer.answer_five = quiz.optA_question_five
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_five = quiz.optB_question_five
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_five = quiz.optC_question_five
                user_answer.save() 
            return redirect('question6', user_id)
            
    # user_answer.answerFive_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question5.html', context)


def question6(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerSix_status == True:
        return redirect('question7', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerSix_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_sixC += 1
                user_answer.answer_six = quiz.optA_question_six
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_six = quiz.optB_question_six
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_six = quiz.optC_question_six
                user_answer.save() 
            return redirect('question7', user_id)
            
    # user_answer.answerSix_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question6.html', context)


def question7(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerSeven_status == True:
        return redirect('question9', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerSeven_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_sevenC += 1
                user_answer.answer_seven = quiz.optA_question_seven
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_seven = quiz.optB_question_seven
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_seven = quiz.optC_question_seven
                user_answer.save() 
            return redirect('question8',user_id)
            
    # user_answer.answerSeven_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question7.html', context)

def question8(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerEight_status == True:
        return redirect('question9', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerEight_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_eightC += 1
                user_answer.answer_eight = quiz.optA_question_eight
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_eight = quiz.optB_question_eight
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_eight = quiz.optC_question_eight
                user_answer.save()
            return redirect('question9',user_id)
            
    # user_answer.answerEight_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question8.html', context)

def question9(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerNine_status == True:
        return redirect('question10', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerNine_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_nineC += 1
                user_answer.answer_nine = quiz.optA_question_nine
                user_answer.full_clean()
                user_answer.save()
                print('option 1 is the answer')
            
            elif selected_option == 'option2':
                user_answer.answer_nine = quiz.optB_question_nine
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_nine = quiz.optC_question_nine
                user_answer.save() 
            return redirect('question10', user_id)
            
    # user_answer.answerNine_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question9.html', context)

def question10(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = user_answer.totalsec()

    if user_answer.answerTen_status == True:
        return redirect('result', user_id)
    else:
        if request.method == 'POST':
            user_answer.answerTen_status = True
            selected_option = request.POST['answers']
            if selected_option == 'option1':
                user_answer.answer_tenC += 1
                user_answer.answer_ten = quiz.optA_question_ten
                user_answer.full_clean()
                user_answer.save()
                return redirect('result', user_id)
            
            elif selected_option == 'option2':
                user_answer.answer_ten = quiz.optB_question_ten
                user_answer.save()
            
            elif selected_option == 'option3':
                user_answer.answer_ten = quiz.optC_question_ten
                user_answer.save() 
            return redirect('result', user_id)
    
        # user_answer.answerTen_status = True
        user_answer.total = total
        user_answer.save()
    context = {
        'quiz':quiz
    }
    return render (request, 'question10.html', context)

def result(request, user_id):
    quiz = Quiz.objects.get()
    user_answer = UserAnswer.objects.get(pk=user_id)
    total = UserAnswer.totalsec

    context={
        'quiz':quiz,
        'user_answer':user_answer,
        'total':total
    }
    return render(request, 'result.html', context)






def legend(request):
    if request.method == 'POST':
        legend = UploadForm(request.POST)
        if legend.is_valid:
            legend.save()
            return redirect('legend')
    else:
        legend = UploadForm()

    context = {
        'legend':legend
    }
    return render(request, 'legend.html', context)