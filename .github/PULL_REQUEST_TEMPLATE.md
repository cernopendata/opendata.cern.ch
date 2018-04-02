Please start by choosing an appropriate base branch for your pull request.

- ``production`` branch: should not be used for pull requests; it is fast-forwarded to `qa` branch at chosen points in time for production deployments;

- ``qa`` branch: shorter-term rollout nature (think a few days); used for fixes and new features observed on the production service; should be a good default branch for most pull requests;

- ``master`` branch: longer-term rollout nature (think a few weeks); bigger developments that may need longer stabilisation periods and iterations with the experiments.

Please reference all issues that this PR addresses or closes. Do not forget to include ``(addresses #123)`` or ``(closes #123)`` in your commit log message.

Please run the tests locally in order to speed up developments and save Travis CI cycles.  Look for ``./run-tests.sh``.

Finally, if you are a member of the ``cernopendata`` team, please select an appropriate issue labels and the concrete milestone to ease our housekeeping.

Checklist:
- [ ] Verified that the system builds and works locally as described?
- [ ] Added tests to ensure success and verified failures?
- [ ] Updated the documentation?
- [ ] Described the nature of the change in a self-understandable commit log
      message?

This message should be replaced with the description of the pull request at hand.

Thank you.
