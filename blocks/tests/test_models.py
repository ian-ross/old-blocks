from django.contrib.auth.models import User
from django.db.utils import IntegrityError

import pytest

from blocks.models import Project


@pytest.mark.django_db
def test_project_create():
    u = User.objects.create_user('test@example.com')
    p = Project.objects.create(user=u, name='Test project',
                               baseline=24, bonus=0, rows=4)
    assert p.pk == 1

    
@pytest.mark.django_db
def test_project_name_uniqueness():
    u = User.objects.create_user('test@example.com')
    with pytest.raises(IntegrityError):
        p1 = Project.objects.create(user=u, name='Duplicate project',
                                    baseline=24, bonus=0, rows=4)
        p2 = Project.objects.create(user=u, name='Duplicate project',
                                    baseline=24, bonus=0, rows=4)
    
    