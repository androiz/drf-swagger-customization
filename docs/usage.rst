=====
Usage
=====

With this package we can increase the auto-generated documentation from django-swagger. That way, we can add documentation
from external APIs or add more information to our drf API methods such as fields, remove endpoints, update attributes, and so on.

Add these global variables to your settings.py:

.. code-block:: python

    EXTENSION_PATH = os.path.join(PROJECT_DIR, 'docs/doc_extension.json') # Path to your extension file
    EXTERNAL_DOC_FOLDER = os.path.join(PROJECT_DIR, 'docs/external/') # Path to your external documentation folder


Add drf-swagger-customization's URL patterns:

.. code-block:: python

    from drf_swagger_customization.views import get_swagger_view

    schema_view = get_swagger_view(title='Pastebin API')

    urlpatterns = [
        ...
        url(r'^docs/$', schema_view),
        ...
    ]

Building the JSON File
----------------------

In order to add information to our EXTENSION_PATH json file,  we have available these operations:

Create:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    {
        "operation": "create",
        "swagger-data": {
            "paths|/v1/travels/|get|parameters": [
                {
                  "name": "Field1",
                  "in": "query",
                  "required": true,
                  "type": "string"
                },
                {
                  "name": "Field2",
                  "in": "path",
                  "required": true,
                  "type": "integer"
                }
            ]
        }
    }

Update:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    {
        "operation": "update",
        "swagger-data": {
            "paths|/v1/travels/|get|parameters|field1": {
                "name": "Field1",
                "in": "query",
                "required": true,
                "type": "string"
            }
        }
    }

Remove:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    {
        "operation": "delete",
        "swagger-data": "paths|/v1/travels/|get|parameters|field1"
    }

Rename
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    {
        "action": "rename",
        "operation": {
            "paths|/v1/travels/": "/travels/",
            "paths|/v1/travels/{id}/": "/travels/{id}/"
        }
    }

Completed Sample
----------------

.. code-block:: javascript

    [
      {
        "operation": "create",
        "swagger-data": {
          "paths|/v1/travels/|get|parameters": [
            {
              "name": "Field1",
              "in": "query",
              "required": true,
              "type": "string"
            },
            {
              "name": "Field2",
              "in": "path",
              "required": true,
              "type": "integer"
            }
          ]
        }
      },
      {
        "operation": "update",
        "swagger-data": {
          "paths|/v1/travels/|get|parameters|field1": {
            "name": "Field1",
            "in": "query",
            "required": true,
            "type": "string"
          }
        }
      },
      {
        "operation": "delete",
        "swagger-data": "paths|/v1/travels/|get|parameters|field1"
      },
      {
        "action": "rename",
        "operation": {
            "paths|/v1/travels/": "/travels/",
            "paths|/v1/travels/{id}/": "/travels/{id}/"
        }
      }
    ]
