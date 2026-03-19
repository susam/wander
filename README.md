Wander Console - Browse the Small Web
=====================================

**Wander** is a small, decentralised, self-hosted web console that
lets your visitors explore random pages from a community of personal
websites.

[![Wander][IMG]][CON]

Each Wander console loads personal websites and pages recommended by
the Wander community.  Further, each Wander console can link to other
Wander consoles, forming a lightweight, decentralised network for
browsing the small web of personal websites.

Visit https://susam.net/wander/ to see an example of a Wander console.

[IMG]: https://susam.github.io/blob/img/wander/wander-0.1.0.png
[CON]: https://susam.net/wander/


Contents
--------

* [How It Works](#how-it-works)
* [Wandering the Web](#wandering-the-web)
* [Setup](#setup)
* [Caution](#caution)
* [Design](#design)
* [Comparisons](#comparisons)
  * [Wander vs Kagi Small Web](#wander-vs-kagi-small-web)
  * [Wander vs StumbleUpon](#wander-vs-stumbleupon)
  * [Wander vs Webrings](#wander-vs-webrings)
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
  Wander console user interface.

- [wander.js](wander.js) - This is where you define the list of
  websites and pages you recommend and the other Wander consoles you
  want your console to link to.  The other Wander consoles you link to
  are known as the neighbours of your console.  So this file defines
  your console neighbourhood.

Together, these two files form a Wander console.  The most interesting
aspect of the Wander console is that everything happens on the
client-side, on the user's web browser.  As a website owner, you do
not need to set up any server-side components.  The only thing you
need to do is place the above two files somewhere on your web server,
preferably, at the directory `/wander/`.


Wandering the Web
-----------------

A visitor begins wandering at a Wander console.  This might be your
own console or someone else's.  For example, you could start wandering
at https://susam.net/wander/ right now.

Once on a Wander console, the visitor can click the Wander button
at the top left to visit websites and pages recommended by the
community.

The first time you load someone's Wander console, one of the web pages
recommended by the console owner is picked randomly and presented to
you.  The console you are on then discovers all the other consoles
that the console owner has linked to in their `wander.js` file.  These
other consoles are known as the neighbours of the first console (the
one you visited).

When you click the **Wander** button for the first time, one of these
neighbouring consoles is chosen at random.  A page recommended by that
console is then shown to you.  At the same time, the neighbours of
that console are discovered as well.  Note that throughout this
process, you remain on the original console you visited.

With each click of the button, a console is chosen at random from the
growing list of discovered consoles.  Specifically, it selects a
random console from the most recently discovered 1000 consoles.  A
recommendation from that console is shown to you and its neighbours
are added to the list.  In this way, each hop takes you deeper into
the Wander network, while expanding the set of known consoles.

As mentioned earlier, you never leave the original console while this
happens.  However, if you wish, you can click the **Console** button
at the top to move to a neighbour's console.  In practice, this is
rarely necessary since most consoles look similar, but you can do so
if you want to explore a different console.  Occasionally, some
console owners style their consoles differently, so you may encounter
a few quirky consoles when switching consoles.


Setup
-----

1. Download this bundle:
   https://codeberg.org/susam/wander/archive/wander.zip

2. Extract the following files:

   - `index.html`
   - `wander.js`

   These are the only two files you need.  You can delete everything
   else.

3. Place them on your website, for example:

   ```
   wander/
   ├── index.html
   └── wander.js
   ```

4. Open `wander.js` and edit the following JavaScript object:

   ```javascript
   window.wander = {
     consoles: [],
     pages: [],
   }
   ```

   Please see https://susam.net/wander/wander.js for an example.

   The value for the `consoles` property is a list of console URLs
   that you want to link to from your console.  This defines your
   console's neighbourhood.  When a user visits your console, it
   fetches the `wander.js` files of these neighbouring consoles to
   discover website recommendations.  These console links are also
   shown when the user clicks the **Console** button on your console.
   Further, when another console reaches your console while exploring
   the network, it follows these links to discover recommendations
   from your neighbourhood.

   The value for the `pages` property is a list of websites and pages
   that you want to recommend to the Wander community.  When a user
   visits your console, a recommendation is chosen at random from this
   list and displayed.  Likewise, when another console reaches your
   console, it uses this list to pick a recommendation at random and
   present it to its user.

5. Once your console is live, share it with others in the following
   community thread: [codeberg.org/susam/wander/issues/1][thread]

   Hopefully, someone will link to your console and then visitors to
   their console may receive recommendations from your `wander.js`.

[thread]: https://codeberg.org/susam/wander/issues/1


Caution
-------

When adding links to your console, make sure each one loads
successfully within the console.  Some websites set the
`X-Frame-Options` HTTP header or the `frame-ancestors` directive in
their `Content-Security-Policy` header to prevent their pages from
being embedded in other websites.  Such pages will not load inside the
Wander console.

Adding such links to your `wander.js` can disrupt the wandering
experience for users of the Wander network.

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
consoles are equal participants from a technical perspective.  None of
them act as a canonical source of seed URLs.  The network is defined
entirely by these independently hosted consoles.  A visitor can start
from any one of them and browse the network.  With each click, the
console tool simply follows the console neighbourhood from one console
to another and loads the recommended pages it discovers.


Comparisons
-----------

Wander is often compared to other projects and trends like webrings,
Kagi Small Web and StumbleUpon.  There is indeed a lot of similarity
between Kagi and such projects.  After all, each such service has been
an inspiration behind Wander.  While there is a lot of similarity with
such services, there are some differences as well.  These differences
are noted in the following subsections.

### Wander vs Kagi Small Web

[Kagi Small Web][kagi] currently accepts only blogs, comics and
YouTube channels.  It does not accept arbitrary small websites.  In
fact, it was this particular limitation that motivated me to build
Wander.

Unlike Kagi Small Web, there is no central list of URLs.  Each
participant hosts their own Wander console along with their own list
of favourite URLs.  You can begin browsing the network from any
console.  The pages you see are pulled from that console, the consoles
it links to and so on recursively.

[kagi]: https://kagi.com/smallweb/


### Wander vs StumbleUpon

Wander has similarities to [StumbleUpon][stumble] as well but unlike
StumbleUpon there is no central service.  The Wander network lives
entirely on independent personal websites maintained by individuals.
The pages shown in a console come directly from such Wander consoles
that belong to individual personal website owners.


### Wander vs Webrings

Wander is similar to webrings in spirit, but differs in structure.  A
typical webring forms a cycle, where each site links to a fixed next
and previous site.  In Wander, the network graph is arbitrary.  Each
instance can link to any number of pages and other instances.

There is no central list and no ring maintainer deciding how sites are
connected.  With Wander, *you* decide which pages to recommend and
which other consoles to link to.  This means you are in full control
of your recommendations and your Wander neighbourhood.

[stumble]: https://en.wikipedia.org/wiki/StumbleUpon


Support
-------

I put this together in the early hours of morning today (18 Mar 2026),
so it may not be very polished and the list of websites is quite small
as well.  But the list is growing.  I am adding some finishing touches
too whenever I can spare some time from my otherwise busy schedule.
If you encounter a bug, [please let me know][ISSUES].  If you like the
idea, I would be glad if you [join the network](#setup).

[ISSUES]: https://codeberg.org/susam/wander/issues


Licence
-------

This is free and open source software.  You can use, copy, modify,
merge, publish, distribute, sublicence and/or sell copies of it, under
the terms of the MIT Licence.  See [LICENCE.md][L] for details.

This software is provided "AS IS", WITHOUT WARRANTY OF ANY KIND,
express or implied.  See [LICENCE.md][L] for details.

[L]: LICENCE.md
