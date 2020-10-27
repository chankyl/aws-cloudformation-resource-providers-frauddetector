from aws_frauddetector_outcome.helpers import model_helpers
from unittest.mock import MagicMock
from .. import unit_test_utils


def test_get_model_for_outcome():
    # Arrange
    list_tags_response = {'tags': unit_test_utils.FAKE_TAGS}

    mock_afd_client = unit_test_utils.create_mock_afd_client()
    mock_afd_client.list_tags_for_resource = MagicMock(return_value=list_tags_response)

    # Act
    model_for_outcome = model_helpers.get_model_for_outcome(mock_afd_client, unit_test_utils.FAKE_OUTCOME)

    # Assert
    assert mock_afd_client.list_tags_for_resource.call_count == 1
    assert model_for_outcome == unit_test_utils.create_fake_model(is_output_model=True)
