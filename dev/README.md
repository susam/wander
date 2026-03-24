Developer Notes
===============

Release Checklist
-----------------

 1. Update version number in [Makefile](Makefile).

 2. Obtain a new screenshot if necessary:

    ```
    make ss
    ```

 3. Update copyright in [LICENCE.md][].
 4. Update [CHANGES.md][]
 5. Update version number in this file (2 places).
 6. Update version number in [index.html][] (2 places).
 7. Run the following commands:

    ```
    make checks
    git status
    git add -p

    VER=0.2.0
    git commit -m "Set version to $VER"
    git tag "$VER" -m "Wander $VER"
    make push
    git push cb "$VER"
    git push gh "$VER"
    ```

 8. Write release page on personal website:

    ```sh
    cd ~/git/susam.net/
    git checkout main
    em content/tree/code/news/wander/$VER.post.html
    ```

 9. Commit personal website:

    ```
    VER=0.2.0
    cd ~/git/susam.net/
    git checkout main
    cp ~/git/wander/index.html content/tree/wander/
    git status
    git add -p
    git add content/tree/wander/
    git commit -m "Add Wander version $VER"
    git log -n 1 --stat
    git push
    ```

10. Publish personal website:

    ```
    git checkout cu
    git rebase main
    make cu
    ```

11. Make a new release on Codeberg.

12. Make a new release on GitHub.

13. Share on Mastodon.

14. Share on newsletter.

15. Share on IRC.

[LICENCE.md]: ../LICENCE.md
[CHANGES.md]: ../CHANGES.md
[index.html]: ../index.html
