from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from grandchallenge.core.validators import ExtensionValidator
from grandchallenge.jqfileupload.widgets import uploader
from grandchallenge.jqfileupload.widgets.uploader import UploadedAjaxFileList
from grandchallenge.mlmodels.models import MLModel

mlmodel_upload_widget = uploader.AjaxUploadWidget(
    ajax_target_path="ajax/model-upload/", multifile=False
)


class MLModelForm(forms.ModelForm):
    chunked_upload = UploadedAjaxFileList(
        widget=mlmodel_upload_widget,
        label="Model Container",
        validators=[
            ExtensionValidator(allowed_extensions=(".tar", ".tar.gz"))
        ],
        help_text=(
            ".tar.gz archive of the container image produced from the command "
            "'docker save IMAGE > IMAGE.tar | gzip'. See "
            "https://docs.docker.com/engine/reference/commandline/save/"
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit("save", "Submit", css_class="d-none"))

    class Meta:
        model = MLModel
        fields = ["chunked_upload", "requires_gpu"]
