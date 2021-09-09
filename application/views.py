from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        my_uploaded_file = request.FILES['uploaded_file'].size



        ques = ['Can we use multiple filters?',
                'Can we do negative slicing?',
                'Can we order data in descending order?',
                'Can we display size of file?']

        ans1 = 'Yes, we can use multiple filters by using pipes, for this one, as an example I have used title and truncatechars filter together'

        ans2 = 'Yes, we can do negative slicing, it works the same as normal python. I have done -5: slicing in this one'

        ans3 = 'Yes, we can, using dictsortreversed'
        ans3_dict = [
            {'name': 'Ishika', 'age': 21},
            {'name': 'avantika', 'age': 25},
            {'name': 'Naitik', 'age': 30},
            {'name': 'Riya', 'age': 15}
        ]

        ans4 = 'Yes, using the size attribute of a uploaded file'

        answers = [ans1, ans2, ans3, ans4]

        qa = {}
        for i in range(4):
            qa[ques[i]] = answers[i]

        return render(request, 'application/answers.html', {'qa': qa,
                                                            'q3dict': ans3_dict,
                                                            'file': my_uploaded_file})
    else:
        return render(request, 'application/answers.html')