**Django Bootstrap**

Django class-based views ready to work with Twitter's Bootstrap toolkit, designed to kickstart development of webapps and sites.

**Installation**

1. Install through pip (or manually place it on your `PYTHON_PATH`).

    `pip install git+http://github.com/codasus/django-bootstrap#egg=bootstrap`

**Example**

urls.py

```python
...

urlpatterns = patterns('',
    url('^', include('contact_list.urls', namespace='contact_list')),
)
```

contact_list/models.py

    Take a look at `test_app/contact_list/models.py`

contact_list/forms.py

```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
```

contact_list/urls.py

```python
from bootstrap.urls import bootstrap_patterns
from contact_list.forms import ContactForm

urlpatterns = bootstrap_patterns(ContactForm)
```

Well done! Just go to http://localhost:8000/contact

**License**

Django Bootstrap by [Codasus Technologies](http://codasus.com) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

You are free:

* to Share - to copy, distribute and transmit the work
* to Remix - to adapt the work
* to make commercial use of the work
