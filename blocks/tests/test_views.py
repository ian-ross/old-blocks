from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

import pytest

from ..models import Project
from ..views import ProjectListView


@pytest.mark.django_db
def test_project_list_view():
    user = User.objects.create_user('test@example.com')
    ps = [Project.objects.create(user=user, name=f'Project #{i+1}',
                                 baseline=12, rows=3)
          for i in range(4)]
    c = Client()
    c.force_login(user)
    resp = c.get(reverse('blocks:project_list'))
    assert resp.status_code == 200
    assert 'Project #1' in str(resp.content)
    