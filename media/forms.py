# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django import forms

# =============================================================================
# CLASSES
# =============================================================================


class UploadForm(forms.Form):
    file0 = forms.FileField(label='')
    file1 = forms.FileField(label='')
    file2 = forms.FileField(label='')
    file3 = forms.FileField(label='')
    file4 = forms.FileField(label='')

    number_of_files = range(5)
