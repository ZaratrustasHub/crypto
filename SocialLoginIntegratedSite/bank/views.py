from django.shortcuts import render
from django.http import HttpResponse
from bank.forms import TransactionForm, CustomerForm

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Please Login to manage your account"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'bank/index.html', context_dict)

def loggedin(request):
    return render(request, 'bank/loggedin.html')

def transaction_history(request):
    latest_question_list = Transactions.objects.order_by('-pub_date')[:50]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)

def add_customer(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the loggedin() view.
            # The user will be shown the loggedin page.
            return loggedin(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CustomerForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'bank/add_customer.html', {'form': form})

def before_action_form(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('template.html',locals())


def new_transaction(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return loggedin(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TransactionForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'bank/new_transaction.html', {'form': form})

