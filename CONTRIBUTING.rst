============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/ciscoucs/imcsdk/issues.

If you are reporting a bug, please include:

* Console logs and stack trace, if any.
* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submitting pull requests to change the documentation or code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changes can be proposed by sending a pull request (PR). A maintainer will
review the changes and provide feedback.

The pull request will be merged into the master branch after discussion.

Please make sure to run the tests and that the tests pass before submitting the
PR. Please keep in mind that some changes might not be merged if the
maintainers decide they can't be merged.

Please squash your commits to one commit per fix or feature. The resulting
commit should have a single meaningful message.

Additions/Modifications done to the apis layer should conform to the following:-
- add/create/set/modify functions should return the corresponding Managed Object
- as much as possible every api should ideally be accompanied with it's testcase
 
Testing your code
~~~~~~~~~~~~~~~~~
Some test cases are written to be run against live hardware.  You will need a
real server available to run them.  Edit the tests/connection/connection.cfg
file and set the hostname, username, and password to match your server.  e.g.

    [imc]
    
    hostname=192.168.1.1
    
    username=admin
    
    password=password

The test suite is typically run via nose as follows:

    nosetests -vs

or if you only want to run tests in a specific file (e.g. test_power.py):

    nosetests -vs tests/server/test_power.py

Commit message guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~

The short summary should include the name of the directory or file affected by
the commit (e.g.: utils: added a new utility method to get status).

A longer description of what the commit does should start on the third line
when such a description is deemed necessary.

If you have trouble with the appropriate git commands to handle these
requirements, please let us know! We're happy to help.

Legal Stuff: Sign your work
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must sign off on your work by adding your signature at the end of the
commit message. Your signature certifies that you wrote the patch or otherwise
have the right to pass it on as an open-source patch.

If you set your user.name and user.email git configuration options, you can
sign your commits automatically with `git commit -s`.

    git config user.name "Joe Smith"

    git config user.email joe.smith@email.com

`git commit -s` should be used now to sign the commits automatically, instead of
git commit.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/ciscoucs/imcsdk/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)
