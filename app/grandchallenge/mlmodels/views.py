from django.views.generic import CreateView
from rest_framework import viewsets, permissions

from grandchallenge.core.permissions.mixins import UserIsStaffMixin
from grandchallenge.mlmodels.forms import MLModelForm
from grandchallenge.mlmodels.models import MLModel
from grandchallenge.mlmodels.serializers import MLModelSerializer


class MLModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer
    permission_classes = (permissions.IsAdminUser,)


class MLModelCreate(UserIsStaffMixin, CreateView):
    model = MLModel
    form_class = MLModelForm

    def form_valid(self, form):
        form.instance.creator = self.request.user

        uploaded_file = form.cleaned_data["chunked_upload"][0]
        form.instance.staged_image_uuid = uploaded_file.uuid

        return super().form_valid(form)
