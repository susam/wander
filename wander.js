const wander = {
  // Other Wander consoles that visitors can reach from my console.
  consoles: [
    'https://susam.net/wander/',
  ],

  // My favourite websites and pages I recommend to the Wander community.
  pages: [
    'https://susam.net/',
    'https://susam.net/invaders.html',
  ],

  // Websites and consoles to ignore.  My console will never fetch
  // consoles or web pages whose URLs match the following patterns.
  ignore: [
    // Out of scope.  These are commercial platforms, not personal websites.
    'https://medium.com/',
    'https://substack.com/',

    // These pages fail to load in the console due to frame restrictions.
    'https://cari.institute/',
    'https://wdl.mcdaniel.edu/',
  ]
}
