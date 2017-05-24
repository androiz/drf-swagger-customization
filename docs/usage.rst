=====
Usage
=====

To use drf-swagger-customization in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_swagger_customization.apps.DrfSwaggerCustomizationConfig',
        ...
    )

Add drf-swagger-customization's URL patterns:

.. code-block:: python

    from drf_swagger_customization import urls as drf_swagger_customization_urls


    urlpatterns = [
        ...
        url(r'^', include(drf_swagger_customization_urls)),
        ...
    ]
