Developer Notes
===============

Release Checklist
-----------------

 1. If taking a new screenshot, update version number in `Makefile`.
    Then take a new screenshot:

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

    VER=0.3.0
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

 9. Commit and push personal website.

10. Make a new release on Codeberg.

11. Make a new release on GitHub.

12. Share on Mastodon.

13. Share on newsletter.

14. Share on IRC.

[LICENCE.md]: ../LICENCE.md
[CHANGES.md]: ../CHANGES.md
[index.html]: ../index.html
