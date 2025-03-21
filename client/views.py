from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from writer.models import Article

from .models import Subscription


@login_required(login_url="my_login")
def client_dashboard(request):
    try:
        subDetails = Subscription.objects.get(user=request.user)
        subPlan = subDetails.subscription_plan
        context = {"SubPlan":subPlan}
        return render(request, "client/client-dashboard.html", context)

    except:
        subPlan = "None"
        context = {"SubPlan":subPlan}

        return render(request, "client/client-dashboard.html", context)

@login_required(login_url="my_login")
def browse_articles(request):
    try:
        #Checks if a user is active on the platform
        subDetails = Subscription.objects.get(user=request.user,
                                              is_active=True)
    except:
        return render(request, "client/sub_lock.html")

    current_subscription_plan = subDetails.subscription_plan

    if current_subscription_plan == "Standard":
        articles = Article.objects.all().filter(is_prem=False)

    elif current_subscription_plan == "Premium":
        articles = Article.objects.all()
    context = {'AllClientArticles': articles}
    return render(request, 'client/browse-articles.html', context)

@login_required(login_url="my_login")
def Subscription_locked(request):
    return render(request, "client/sub_lock.html")