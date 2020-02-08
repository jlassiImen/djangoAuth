
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.forms import profileForm


@login_required
def profile(request):
    if request.method == 'POST':
        form = profileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
    else:
        form = profileForm(instance=request.user)

    return render(request, 'account/dashboard.html', {'form': form})
