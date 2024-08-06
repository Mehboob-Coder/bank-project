from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Bank, Branch
from .forms import BankForm, BranchForm

@login_required
def add_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.save()
            return redirect('/banks/')
    else:
        form = BankForm()
    return render(request, 'add_bank.html', {'form': form})

@login_required
def add_branch(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)

    # if request.user != bank.owner:
    #     return HttpResponse('owner does not found')
    
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank
            branch.save()
            return redirect('branch_details' ,branch_id=branch.id)
    else:
        form = BranchForm(initial={'email': 'admin@enigmatix.io'})
    return render(request, 'add_branch.html', {'form': form , 'bank': bank})

def list_banks(request):
    banks = Bank.objects.all()
    return render(request, 'list_banks.html', {'banks': banks})

def bank_details(request, bank_id):
    bank = Bank.objects.get(id=bank_id)
    branches = Branch.objects.filter(bank=bank)

    banks = Bank.objects.all()
    
    return render(request, 'bank_details.html', {'branches':branches , 'bank': bank , 'banks' : banks})

def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    context = {
        'branch': branch
    }
    return render(request, 'branch_details.html', context)
@login_required
def edit_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.user != branch.bank.owner:
        return HttpResponse(status=403)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect(f'/banks/branch/{branch.id}/details/')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'edit_branch.html', {'form': form})


@login_required
def edit_bank(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    
    if request.user != bank.owner:
        return HttpResponse(status=403)  
    
    if request.method == 'POST':
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()  
            return redirect('bank_details', bank_id=bank.id) 
    else:
        form = BankForm(instance=bank)
    
    return render(request, 'edit_bank.html', {'form': form, 'bank': bank})


@login_required
def delete_bank(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    if request.user != bank.owner:
        return HttpResponse(status=403)  
    if request.method == 'POST':
        bank.delete() 
        return redirect('list_banks')  
    return render(request, 'confirm_delete.html', {'object': bank, 'object_type': 'bank'})


@login_required
def delete_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.user != branch.bank.owner:
        return HttpResponse(status=403) 
    if request.method == 'POST':
        branch.delete()  
        return redirect('bank_details', bank_id=branch.bank.id)  
    return render(request, 'confirm_delete.html', {'object': branch, 'object_type': 'branch'})

