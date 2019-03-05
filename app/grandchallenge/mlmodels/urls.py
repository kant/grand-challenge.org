from django.urls import include, path
from rest_framework.routers import DefaultRouter

from grandchallenge.mlmodels.forms import mlmodel_upload_widget
from grandchallenge.mlmodels.views import MLModelViewSet, MLModelCreate

app_name = "mlmodels"

router = DefaultRouter()
router.register(r"", MLModelViewSet)

urlpatterns = [
    path("create/", MLModelCreate.as_view(), name="mlmodel-create"),
    path(
        f"create/{mlmodel_upload_widget.ajax_target_path}",
        mlmodel_upload_widget.handle_ajax,
        name="mlmodel-upload-ajax",
    ),
    path("", include(router.urls)),
]
