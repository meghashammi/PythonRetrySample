# PythonRetrySample

A simple Design where the Django http request is trying to access 3rd part github library.
The Rest API network calls is wrapped with the retries.
A backoff factor is used to apply between attempts after the second try.

