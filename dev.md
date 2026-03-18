Developer Notes
===============

Release Checklist
-----------------

 1. Update copyright in [LICENCE.md][].
 2. Update [CHANGES.md][]
 3. Update version number in this file (2 places).
 4. Update version number in [index.html][] (2 places).
 3. Run the following commands:

    ```
    make checks
    git status
    git add -p

    VER=0.1.0
    git commit -m "Set version to $VER"
    git tag "$VER" -m "Wander $VER"
    make push
    ```

 4. Write release page on personal website:

    ```sh
    cd ~/git/susam.net/
    git checkout main
    em content/tree/code/news/wander/$VER.post.html
    ```

 5. Commit personal website:

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

 6. Publish personal website:

    ```
    git checkout cu
    git rebase main
    make cu
    ```

 7. Make a new release on Codeberg.

 8. Make a new release on GitHub.

 9. Share on Mastodon.

10. Share on newsletter.

11. Share on IRC.

[LICENCE.md]: LICENCE.md
[CHANGES.md]: CHANGES.md
[index.html]: index.html
