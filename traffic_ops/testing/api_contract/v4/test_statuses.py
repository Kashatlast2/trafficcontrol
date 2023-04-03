#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""API Contract Test Case for statuses endpoint."""
import json
import logging
import os
import pytest
import requests

from trafficops.tosession import TOSession

# Create and configure logger
logger = logging.getLogger()

primitive = bool | int | float | str | None

@pytest.mark.parametrize('request_template_data', ["statuses"], indirect=True)
def test_status_contract(
	to_session: TOSession,
	request_template_data: list[dict[str, object] | list[object] | primitive],
	response_template_data: list[dict[str, object] | list[object] | primitive],
	status_post_data: dict[str, object]
) -> None:
	"""
	Test step to validate keys, values and data types from statuses endpoint
	response.
	:param to_session: Fixture to get Traffic Ops session.
	:param get_status_data: Fixture to get Status data from a prerequisites file.
	:param status_prereq: Fixture to get sample Status data and actual Status response.
	"""
	# validate Status keys from statuses get response
	logger.info("Accessing /statuses endpoint through Traffic ops session.")

	status = request_template_data[0]
	if not isinstance(status, dict):
		raise TypeError("malformed status in prerequisite data; not an object")

	status_name = status.get("name")
	if not isinstance(status_name, str):
		raise TypeError("malformed status in prerequisite data; 'name' not a string")

	status_get_response: tuple[
		dict[str, object] | list[dict[str, object] | list[object] | primitive] | primitive,
		requests.Response
	] = to_session.get_statuses(query_params={"name": status_name})
	try:
		status_data = status_get_response[0]
		if not isinstance(status_data, list):
			raise TypeError("malformed API response; 'response' property not an array")

		first_status = status_data[0]
		if not isinstance(first_status, dict):
			raise TypeError("malformed API response; first Status in response is not an object")
		status_keys = set(first_status.keys())

		logger.info("Status Keys from statuses endpoint response %s", status_keys)
		response_template = response_template_data.get("status").get("properties")
		# validate status values from prereq data in statuses get response.
		prereq_values = [
			status_post_data["name"],
			status_post_data["description"],
		]
		get_values = [first_status["name"], first_status["description"], first_status["dnssecEnabled"]]
		get_types = {}
		for key in first_status:
			get_types[key] = first_status[key].__class__.__name__
		logger.info("types from status get response %s", get_types)
		response_template_types= {}
		for key in response_template:
			response_template_types[key] = response_template.get(key).get("type")
		logger.info("types from status response template %s", response_template_types)

		assert status_keys == set(response_template.keys())
		assert dict(sorted(get_types.items())) == dict(sorted(response_template_types.items()))
		assert get_values == prereq_values
	except IndexError:
		logger.error("Either prerequisite data or API response was malformed")
		pytest.fail("Either prerequisite data or API response was malformed")
	finally:
		# Delete Status after test execution to avoid redundancy.
		try:
			status_id = status_post_data["id"]
			to_session.delete_status_by_id(status_id=status_id)
		except IndexError:
			logger.error("Status returned by Traffic Ops is missing an 'id' property")
			pytest.fail("Response from delete request is empty, Failing test_get_status")

