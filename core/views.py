from django.shortcuts import render
from django.conf import settings
import requests
from github import Github, GithubException
from .forms import DictionaryForm
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    return session

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests_retry_session().get(url)
        print("response=====",response)
        print(response.status_code)
        s = requests.Session()
        s.auth = ('user', 'pass')
        s.headers.update({'x-test': 'true'})

        response = requests_retry_session(session=s).get(url)
        print("response===session==",response)
        print(response.status_code)

        user = response.json()
    return render(request, 'core/github.html', {'user': user})
