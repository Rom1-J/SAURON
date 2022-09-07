|image0| |image1| |image2| |image3|


SAURON
======

Acronym: todo...


Project Purpose
---------------

todo...

How does it work ?
~~~~~~~~~~~~~~~~~~

todo...

Things to know
~~~~~~~~~~~~~~

todo...

--------------


Settings
--------

Moved to `settings <http://cookiecutter-django.readthedocs.io/en/latest/settings.html>`_.


Basic Commands
--------------

Setting Up Your Users
~~~~~~~~~~~~~~~~~~~~~

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
- To create a **superuser account**, use this command:

.. code-block:: bash

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Type checks
~~~~~~~~~~~

Running type checks with mypy:

.. code-block:: bash

    $ mypy sauron


Test coverage
~~~~~~~~~~~~~

To run the tests, check your test coverage, and generate an HTML coverage report:

.. code-block:: bash

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html


Running tests with pytest
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ pytest


Live reloading and Sass CSS compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Moved to `Live reloading and SASS compilation <https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading>`_.


Email Server
~~~~~~~~~~~~

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [MailHog](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface will be available.

1.  `Download the latest MailHog release <https://github.com/mailhog/MailHog/releases>`_ for your OS.

2.  Rename the build to `MailHog`.

3.  Copy the file to the project root.

4.  Make it executable:

.. code-block:: bash

        $ chmod +x MailHog

5.  Spin up another terminal window and start it there:

.. code-block:: bash

        ./MailHog

6.  Check out `<http://127.0.0.1:8025/>`_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.


Sentry
~~~~~~

Sentry is an error logging aggregator service. You can sign up for a free account at `<https://sentry.io/signup/?code=cookiecutter>`_ or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.

Refer to `INSTALL.rst <./INSTALL.rst>`_


.. |image0| image:: https://img.shields.io/badge/python-3.10-%23007ec6
.. |image1| image:: https://img.shields.io/github/issues/Rom1-J/SAURON
.. |image2| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. |image3| image:: https://wakatime.com/badge/github/Rom1-J/SAURON.svg
    :target: https://wakatime.com/badge/github/Rom1-J/SAURON
