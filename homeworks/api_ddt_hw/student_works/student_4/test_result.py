import pytest
import json
from configuration import OUTPUT_FILE_PATH
from src.pydantic_schemas.user import User


@pytest.mark.parametrize("result_file_path", [OUTPUT_FILE_PATH+"result.json"])
def test_result_json(result_file_path):
    """Throws a ValueError if the file you pass can't be decoded as JSON."""
    with open(result_file_path, "r") as json_file:
        json.load(json_file)


@pytest.mark.parametrize("result_file_path, model", [(OUTPUT_FILE_PATH+"result.json", User)])
def test_result_structure(result_file_path, model, get_json):
    """Validates json structure with pydantic schema"""
    result = get_json(result_file_path)

    if isinstance(result, list):
        for item in result:
            model.model_validate(item)
    else:
        model.model_validate(result)