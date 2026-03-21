window.wander = {
  // Other Wander consoles that visitors can reach from my console.
  consoles: [
    'https://susam.net/wander/',
  ],

  // My favourite websites and pages I recommend to the Wander community.
  pages: [
    'https://susam.net/',
    'https://susam.net/invaders.html',
  ],

  // Websites and consoles to ignore.  When this console serves as
  // your host console, it will never contact consoles or recommend
  // web pages with addresses that match the following regular
  // expression patterns.
  ignore: [
    // Off-topic since these are commercial services, not personal websites.
    '.*://medium\\.com/.*',
    '.*://substack\\.com/.*',

    // These do not load in the console due to frame-embedding restrictions.
    '.*://cari\\.institute/.*',
    '.*://wdl\\.mcdaniel\\.edu/.*',
  ]
}
