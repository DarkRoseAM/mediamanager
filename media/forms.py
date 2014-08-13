# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django import forms

# =============================================================================
# CLASSES
# =============================================================================

class ManifestForm(forms.Form):
    manifest_file = forms.FileField(
        label='Select a manifest file.',
        help_text='This needs to be an xml file.'
    )
