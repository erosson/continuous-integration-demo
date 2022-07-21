# continuous-integration-demo
This is what a git repository with **Continuous Integration (CI)** looks like.

Continuous Integration is *the single best tool* I know of to stop your code from breaking. It's one of the first things I set up in any new codebase. I can't/won't work without it.

---

Maybe you already write automated tests/unit tests. How often do you run those tests, though? Do you know if they're still passing? A test that's been failing for weeks is worse than useless.

Continuous Integration (CI) sets up a robot to automatically run your tests whenever someone opens a pull request, or commits to the main branch. 

With CI, your tests are run much, much more often. This makes those tests more useful: if they fail, it's much easier to track down when they started failing and what caused the failures. Each failing test you fix is one less bug that makes it to production. 

---

The #1 rule of continuous integration: *never let tests in the main branch fail*. If they fail, fixing them immediately should be your top priority - even if that fix is skipping the test and fixing it properly later.

(There's nothing special about the branch name `main` - I mean the primary branch; the default branch; the branch you start developing from.)

When tests in `main` are passing, and tests in your PR are failing, that's a very useful signal. Your PR has probably broken something, and you should fix it!

But when tests in `main` are failing, and tests in your PR are failing, that's not a useful signal. Is this failure the one that was already in `main`? Did your PR break anything new? You can't tell! So, don't let tests in `main` fail - and if they do fail, fix them quickly. Your colleagues will thank you.

Do you already have some tests, and want to set up CI for the first time? Have CI run just the tests that already pass, and skip the failing tests.
