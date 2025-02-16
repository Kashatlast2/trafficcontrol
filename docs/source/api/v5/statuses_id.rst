..
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..     http://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
..

.. _to-api-statuses-id:

*******************
``statuses/{{ID}}``
*******************

``PUT``
=======
Updates a :term:`Status`.

:Auth. Required: Yes
:Roles Required: None
:Permissions Required: STATUS:UPDATE, STATUS:READ
:Response Type:  Array

Request Structure
-----------------
:description:	The description of the updated :term:`Status`
:name:			The name of the updated :term:`Status`

.. code-block:: http
	:caption: Request Example

	PUT /api/5.0/statuses/3 HTTP/1.1
	Host: trafficops.infra.ciab.test
	User-Agent: curl/7.47.0
	Accept: */*
	Cookie: mojolicious=...

	{ "description": "test", "name": "example" }

Response Structure
------------------
:description: A short description of the status
:id:          The integral, unique identifier of this status
:lastUpdated: The date and time at which this status was last modified, in :rfc:3339 format
:name:        The name of the status

.. code-block:: http
	:caption: Response Example

	HTTP/1.1 200 OK
	Access-Control-Allow-Credentials: true
	Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, Set-Cookie, Cookie
	Access-Control-Allow-Methods: POST,GET,OPTIONS,PUT,DELETE
	Access-Control-Allow-Origin: *
	Content-Type: application/json
	Set-Cookie: mojolicious=...; Path=/; Expires=Mon, 18 Nov 2019 17:40:54 GMT; Max-Age=3600; HttpOnly
	Whole-Content-Sha512: dHNip9kpTGGS1w39/fWcFehNktgmXZus8XaufnmDpv0PyG/3fK/KfoCO3ZOj9V74/CCffps7doEygWeL/xRtKA==
	X-Server-Name: traffic_ops_golang/
	Date: Mon, 10 Dec 2018 20:56:59 GMT
	Content-Length: 167

	{ "alerts": [
		{
			"text": "status was created.",
			"level": "success"
		}
	],"response": [
		{
			"description": "test",
			"name": "example"
			"id": 3,
			"lastUpdated": "2018-12-10T19:11:17Z",
		}
	]}

``DELETE``
==========
Deletes a :term:`Status`.

:Auth. Required: Yes
:Roles Required: "admin" or "operations"
:Permissions Required: STATUS:DELETE, STATUS:READ
:Response Type:  Object

Request Structure
-----------------
.. table:: Request Path Parameters

	+------+----------+---------------------------------------------------------------------------------------------+
	| Name | Required | Description                                                                                 |
	+======+==========+=============================================================================================+
	| id   | yes      | The integral, unique identifier of the desired :abbr:`Status`-to-:term:`Server` association |
	+------+----------+---------------------------------------------------------------------------------------------+

.. code-block:: http
	:caption: Request Example

	DELETE /api/5.0/statuses/18 HTTP/1.1
	User-Agent: curl/8.1.2
	Accept-Encoding: gzip, deflate
	Accept: */*
	Connection: keep-alive
	Cookie: mojolicious=...
	Content-Length: 0

Response Structure
------------------
.. code-block:: http
	:caption: Response Example

	HTTP/1.1 200 OK
	Access-Control-Allow-Credentials: true
	Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, Set-Cookie, Cookie
	Access-Control-Allow-Methods: POST,GET,OPTIONS,PUT,DELETE
	Access-Control-Allow-Origin: *
	Content-Encoding: gzip
	Content-Type: application/json
	Set-Cookie: mojolicious=...; Path=/; Expires=Thu, 15 Jun 2023 22:37:37 GMT; Max-Age=3600; HttpOnly
	Whole-Content-Sha512: T8wtKKwyOKKVwDwoNCNvETllsByDiEe4CrpeS7Zdox+rXMgPb3FBlKmmgu4CpxbWdhpiODKqKn+gsSq5K4yvIQ==
	X-Server-Name: traffic_ops_golang/
	Date: Thu, 15 Jun 2023 21:41:18 GMT
	Content-Length: 62

	{
		"alerts": [
			{
				"text": "status was deleted.",
				"level": "success"
			}
		]
	}
