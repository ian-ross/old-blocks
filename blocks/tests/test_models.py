from django.contrib.auth.models import User
from django.db.utils import IntegrityError

import pytest

from ..models import Project


@pytest.mark.django_db
def test_project_create():
    user = User.objects.create_user('test@example.com')
    p = Project.objects.create(user=user, name='Test project',
                               baseline=24, bonus=0, rows=4)
    assert Project.objects.count() == 1

    
@pytest.mark.django_db
def test_project_name_uniqueness():
    user = User.objects.create_user('test@example.com')
    with pytest.raises(IntegrityError):
        Project.objects.create(user=user, name='Duplicate project', baseline=24)
        Project.objects.create(user=user, name='Duplicate project', baseline=24)
