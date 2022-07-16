from django.shortcuts import render
from .forms import CalculatorForm

# Main view to show calculator
def calculator_home(request):
    #If form has been submitted, display the submitted values along with the calculated contract value else display blank form
    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            # Calculate contract price and format
            # Base rate is 5 million per job
            # Plus 650 * the volume of the contract
            # Plus 2% of the collateral value of the contract
            contract_price = "{:,.2f}".format(5000000 + (int(form.cleaned_data['volume']) * 650) + (int(form.cleaned_data['collateral'] * 0.02)))

            return render(request, "index.html", {'form': form, 'contract_price': contract_price})
    else:
        form = CalculatorForm()

        return render(request, "index.html", {'form': form})