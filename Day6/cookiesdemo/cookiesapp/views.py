from django.shortcuts import render

def cookies_and_session_count(request):
    count = int(request.COOKIES.get('count', 0)) + 1
    count1 = int(request.session.get('count1', 0)) + 1
    request.session["count1"] = count1
    
    print(request.session.get_expiry_date())
    
    context = {
        'count': count,
        'count1': count1,
    }
    response = render(request, 'cookiesapptemp/cookiescount.html', context)
    response.set_cookie("count", count)

    return response
