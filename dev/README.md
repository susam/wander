Developer Notes
===============

Release Checklist
-----------------

 1. Obtain a new screenshot if necessary:

    ```
    make ss
    ```

 2. Update copyright in [LICENCE.md][].
 3. Update [CHANGES.md][]
 4. Update version number in this file (2 places).
 5. Update version number in [index.html][] (2 places).
 6. Run the following commands:

    ```
    make checks
    git status
    git add -p

    VER=0.1.0
    git commit -m "Set version to $VER"
    git tag "$VER" -m "Wander $VER"
    make push
    git push cb "$VER"
    git push gh "$VER"
    ```

 7. Write release page on personal website:

    ```sh
    cd ~/git/susam.net/
    git checkout main
    em content/tree/code/news/wander/$VER.post.html
    ```

 8. Commit personal website:

    ```
    VER=0.1.0
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

 9. Publish personal website:

    ```
    git checkout cu
    git rebase main
    make cu
    ```

10. Make a new release on Codeberg.

11. Make a new release on GitHub.

12. Share on Mastodon.

13. Share on newsletter.

14. Share on IRC.

[LICENCE.md]: LICENCE.md
[CHANGES.md]: CHANGES.md
[index.html]: index.html
