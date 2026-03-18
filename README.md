Wander the Small Web
====================

Wander is a small, decentralised, self-hosted web console that lets
your visitors explore random pages from a community of personal
websites.

[![Wander][IMG]][CON]

Each Wander console loads personal websites and pages recommended by
the Wander community.  Further, each Wander console can link to other
Wander consoles, forming a lightweight, decentralised network for
browsing the small web of personal websites.

Visit https://susam.net/wander/ to see an example of Wander console.

[IMG]: https://susam.github.io/blob/img/wander/wander-0.1.0.png
[CON]: https://susam.net/wander/


Contents
--------

* [How It Works](#how-it-works)
* [Wandering the Web](#wandering-the-web)
* [Setup](#setup)
* [Caution](#caution)
* [Design](#design)
* [FAQ](#faq)
* [Support](#support)
* [Licence](#licence)


How It Works
------------

A Wander console does two things:

1. **Wander pages**: It loads a random page from a list of websites
   and pages recommended by the community.

2. **Wander consoles**: It can send the visitor to another Wander
   console on a different website, where they can continue wandering
   the Web using the new Wander console.

A Wander console is just a directory on your web server with two files:

- [index.html](index.html) - This is the HTML tool that implements the
  Wander console.

- [wander.js](wander.js) - This is where you define the list of
  websites and pages you recommend and the other Wander consoles you
  want your console to link to.

The most interesting aspect of Wander console is that everything
happens on the client-side, on the user's web browser.  As a website
owner, you do not need to set up any server-side components.  The only
thing you need to do is place the above two files somewhere on your
webserver, preferrably, at the directory `/wander/`.


Wandering the Web
-----------------

A visitor begins at a Wander console.  This might be your own console
or someone else's.  For example, you could start at
https://susam.net/wander/ right now.

Once on a Wander console, the visitor can click the **Wander** button
at the top left to visit websites and pages recommended by the
community.

The first time you wander, the recommendation comes from the current
console.  The second time you wander, it comes from another console
linked by the first.  The third time you wander, it comes from a
console linked by the second, and so on.  In each hop, a console is
chosen at random from those linked by the previous one.  A website
recommendation is then chosen at random from that console.  In this
way, each hop takes you deeper and deeper into the Wander network.


Setup
-----

1. Download this bundle:
   https://codeberg.org/susam/wander/archive/main.zip

2. Extract the following files:

   - `index.html`
   - `wander.js`

3. Place them on your website, for example:

   ```
   wander
   ├── index.html
   └── wander.js
   ```

4. Open `wander.js` and edit the following JavaScript object:

   ```javascript
   window.wander = {
     consoles: [
     ],
     pages: [
     ],
   }
   ```

   The value for the `pages` property is a list of websites and pages
   you recommend to the community.

   The value for the `consoles` property is a list of consoles your
   console should link to.

   Please see https://susam.net/wander/wander.js for an example.

5. Once your console is live, share it with others in the following
   community thread:

   [codeberg.org/susam/wander/issues/1](https://codeberg.org/susam/wander/issues/1)

   Hopefully, someone will link to your console and then visitors to
   their console may receive recommendations from your `wander.js`.


Caution
-------

When adding links to your console, make sure each one loads
successfully within the console.  Some websites set the
`X-Frame-Options` HTTP header or the `frame-ancestors` directive in
their `Content-Security-Policy` header to prevent their pages from
being embedded in other websites.  Such pages will not load inside the
Wander console.

Adding such links to your `wander.js` can disrupt the wandering
experience for your visitors.

To test a link, open https://susam.net/wander/ (or your own Wander
console), paste the link into the URL textbox (the pale green input
field) and click **Go**.  If the link loads within the console, it is
safe to include.  If it does not, please avoid adding it to your
`wander.js`.


Design
------

One of the design goals with Wander has been to keep it fully
decentralised, similar to the Web itself.  I have tried to avoid
having any centralised list of URLs or seed nodes.  Each Wander
console is just a small, self-hosted node made up of two static files.
Anyone can run it on their own website, define the pages they
recommend and link to other consoles as neighbours.  All Wander
consoles are equal from a technical perspective.  None of them act as
a canonical source of seed URLs.  The network is defined entirely by
these independently hosted consoles.  A visitor can start from any one
of them and browse the network.  With each click The console tool
simply follows the console neighbourhood from one console to another
and loads the recommended pages it discovers.


FAQ
---

 1. How is this different from Kagi Small Web?

    [Kagi Small Web](https://kagi.com/smallweb/) currently accepts
    only blogs, comics and YouTube channels.  It does not accept
    arbitrary small websites.  That limitation motivated me to build
    Wander.

    Unlike Kagi Small Web, there is no central list of URLs.  Each
    participant hosts their own Wander console.  You can begin browsing
    the network from any console.  The pages you see are pulled from
    that console, the consoles it links to and so on recursively.

2. How is this different from StumbleUpon?

   There are some similarities to
   [StumbleUpon](https://en.wikipedia.org/wiki/StumbleUpon) but unlike
   StumbleUpon there is no central service.  The Wander network lives
   entirely on independent personal websites maintained by
   individuals.  The pages shown in a console come directly from the
   recommendations shared by participants in the network.

3. How different is this from Webrings?

   This is similar to webrings in spirit, but differs in structure.  A
   typical webring forms a cycle, where each site links to a fixed
   next and previous site.  In Wander, the network graph is arbitrary.
   Each instance can link to any number of pages and other instances.

   There is no central list and no ring maintainer deciding how sites
   are connected.  With Wander, *you* decide which pages to recommend
   and which other consoles to link to.  This means you are in full
   control of your recommendations and your Wander neighbourhood.


Support
-------

I put this together in a couple of hours early this morning (18 Mar
2026), so it may not be very polished and the list of websites is
quite small as well.  If you encounter a bug, [please let me
know][ISSUES].  If you like the idea, I would be glad if you [join the
network](#setup).

[ISSUES]: https://codeberg.org/susam/wander/issues


Licence
-------

This is free and open source software.  You can use, copy, modify,
merge, publish, distribute, sublicence and/or sell copies of it, under
the terms of the MIT Licence.  See [LICENCE.md][L] for details.

This software is provided "AS IS", WITHOUT WARRANTY OF ANY KIND,
express or implied.  See [LICENCE.md][L] for details.

[L]: LICENCE.md
