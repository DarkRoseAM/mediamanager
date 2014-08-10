from django import forms


class ManifestForm(forms.Form):
    manifest_file = forms.FileField(
        label='Select a manifest file.',
        help_text='This needs to be an xml file.'
    )
