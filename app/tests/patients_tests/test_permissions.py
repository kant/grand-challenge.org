import pytest

from tests.factories import PatientFactory
from tests.utils import validate_staff_only_view

"""" Tests the permission access for Patient Forms """


@pytest.mark.django_db
@pytest.mark.parametrize(
    "view",
    [
        "patients:patient-create",
        "patients:patient-remove",
        "patients:patient-update",
        "patients:patient-display",
    ],
)
def test_patient_form_access(view, client):
    reverse_kwargs = {}
    if view in ("patients:patient-update", "patients:patient-remove"):
        patient = PatientFactory()
        reverse_kwargs.update({"pk": patient.pk})

    validate_staff_only_view(
        viewname=view, client=client, reverse_kwargs=reverse_kwargs
    )