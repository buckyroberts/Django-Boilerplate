Project setup
=============

Setup local configuration for running code on host::

    mkdir -p local
    cp django_boilerplate/project/settings/templates/settings.dev.py ./local/settings.dev.py


Run dependency services::

    make up-dependencies-only


Run server (in a separate terminal)::

    make run-server

This is a technical last line to serve as `end-of-file-fixer` workaround.
