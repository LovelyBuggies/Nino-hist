
Development Guideline
===========================

Nino-hist development is done in a `git`_ repository on `github`_. Continuous integration testing is provided by `travis CI`_, code coverage is measured with
`coveralls.io`_.

.. _`git`: https://git-scm.com/
.. _`github`: https://github.com/
.. _`travis CI`: https://travis-ci.org/
.. _`coveralls.io`: https://coveralls.io/


Repository structure
===========================

Nino-hist's repository structure is very simple, as we are normally not supporting older versions with bugfixes or other complicated things. The *master* branch of the repository is the basis for releases, a release is nothing more than adding a tag to the branch, creating the tarball, etc. The *master* branch should always be in a deployable state, i.e. one should be able to use it as the base for everyday work without worrying about random breakages due to updates. To ensure this, no commit ever goes into the *master* branch without passing the test suite before (see below). The only exception to this rule is if a commit not touches any code files, e.g. additions to the README file or to the documentation (but even in this case, care should be taken that the documentation is still built correctly).

For every feature that a developer works on, a new branch should be opened (normally based on the *master* branch), with a descriptive name (e.g. ``add-matplotlib-support``). Developers should fork the repository and work in their own repository (if working on multiple issues/features, also using branches).


Implementing a feature/fixing a bug
======================================================

Every new feature or bug fix should be done in a dedicated branch and have an issue in the issue database. For bugs, it is important to not only fix the bug but also to introduce a new test case that makes sure that the bug will not ever be reintroduced by other changes. It is often a good idea to first define the test cases (that should fail) and then work on the fix so that the tests pass. As soon as the feature/fix is complete *or* as soon as specific feedback on the code is needed, open a "pull request" to merge the changes from your branch into *master*. In this pull request, others can comment on the code and make suggestions for improvements. New commits to the respective branch automatically appear in the pull request which makes it a great tool for iterative code review. Even more useful, travis will automatically run the test suite on the result of the merge. As a reviewer, always wait for the result of this test (it can take up to 30 minutes or so until it appears) before doing the merge and never merge when a test fails. As soon as the reviewer decides that the branch is ready to merge, he/she can merge the pull request and optionally delete the corresponding branch (but it will be hidden by default, anyway).


Idea list
===========================

We have some preliminary ideas about what is possible or doable. Some concentrations are listed as follows.


Pull-plot pro implementation
--------------------------------

* **Project description:** Release a more professional pull-plot version (i.e., pull-plot-pro) for Hist's pull-plot method 
* **Objective:** 

	* Allow user to customize pull-plot
	* Enable user to select type of plots in the pull-plot
	* Support passing more specific parameters
	* Specify the same properties for different plots, e.g. color, linewidth, linestyle, etc.

* **Possible tools:** `Matplotlib.Axes`_, `Matplotlib.Figure`_
* **Difficulty:** Easy

.. _`Matplotlib.Axes`: https://matplotlib.org/api/axes_api.html?highlight=axes#module-matplotlib.axes
.. _`Matplotlib.Figure`: https://matplotlib.org/api/figure_api.html?highlight=figure#module-matplotlib.figure


GUI design
------------------

* **Project description:** Design a graphic user interface for Nino-hist to simplify users' operations
* **Objective:** 

	* Create GUI playground 
	* Support Nino-hist's functionality

* **Possible tools:** `Tkinter`_, `wxPython`_, `Jython`_
* **Difficulty:** Hard

.. _`Tkinter`: https://docs.python.org/3/library/tkinter.html
.. _`wxPython`: https://wxpython.org/
.. _`Jython`: https://www.jython.org/


Bool axis transformation
------------------------------------

* **Project description:** Expand transformation to Bool axis
* **Objective:** 

	* All transformation operations for Bool axis
	* Allow functional transformation by Callable

* **Possible tools:** `Boost_histogram`_
* **Difficulty:** Medium

.. _`Boost_histogram`: https://boost-histogram.readthedocs.io/en/latest/index.html

