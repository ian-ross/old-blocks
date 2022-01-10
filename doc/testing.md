# Testing

## Setup

 - Want to use `pytest`, but I couldn't figure out how to get it to
   work properly with the additional `apps` directory holding the
   individual Django applications. So I just removed that layer in the
   project layout...
   
 - There's a `config.settings.test` for running tests, which uses the
   local memory backend for email sending.

 - Also got test coverage going using `pytest-cov`.
 