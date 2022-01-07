# Project layout

```
PROJECT ROOT
├── conda-env.yaml            Conda environment export
├── dev-manage                Helper script to run with dev settings
├── doc/                      Documentation
├── LICENSE
├── manage.py                 Usual Django script
├── README.md
├── config                    All top-level configuration
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py           Settings shared between deployments
│   │   ├── local.py          Development settings
│   │   ├── production.py     Production settings
│   │   └── test.py           Test settings
│   ├── urls.py               Project-level URLconf
│   └── wsgi.py
├── apps                      Django applications
│   ├── blocks                Main app: projects, blocks, etc.
│   │   ├── admin.py
│   │   ├── api
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests
│   │   │   └── tests.py
│   │   └── views.py
│   ├── static/               Static files
│   ├── statistics            Statistics app: plots, etc.
│   └── templates             Project-wide templates
│       └── base.html
├── requirements              Deployment-specific requirements files
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
└── requirements.txt
```
