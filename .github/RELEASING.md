# Releasing

## Distribution builds

Pushing a `v*` tag starts the release workflow. It checks that the tag matches
the version in `pyproject.toml`, runs the development checks, and builds a wheel
and source distribution with `uv build`. Both distributions are installed into
isolated environments and tested before they are uploaded as workflow artefacts.

The workflow creates a draft GitHub release with generated release notes.
After approval of the `pypi` environment, it publishes the tested artefacts to
PyPI without rebuilding them.

## Release procedure

Replace `VERSION` below with the release version, such as `6.0.4`.

1. Update the version in `pyproject.toml`, and run `uv lock` to update
   `uv.lock`. Run the [development checks](CONTRIBUTING.md#implementation), and
   commit the changes in a pull request.
2. Once CI passes, approve and merge the pull request into `main`. Update your
   local checkout:

   ```sh
   git switch main
   git pull --ff-only
   ```

3. Confirm the merged commit passes CI, its version matches the intended
   release, and there are no uncommitted package changes. Tag it and push the
   tag:

   ```sh
   git tag -a vVERSION -m "Release xdg-base-dirs VERSION"
   git push origin vVERSION
   ```

4. Wait for the release workflow to build and test the distributions and create
   a draft GitHub release.
5. Inspect the workflow results and generated release notes. Edit the notes as
   needed, then approve the `pypi` job.
6. Confirm publication to PyPI succeeds, then publish the draft GitHub release.
