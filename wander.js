window.wander = {
  // Other Wander consoles that visitors can reach from my console.
  consoles: [
    'https://susam.net/wander/',
  ],

  // My favourite websites and pages I recommend to the Wander community.
  pages: [
    'https://midnight.pub/',
    'https://susam.net/',
    'https://susam.net/fizz-buzz-with-cosines.html'
  ],

  // Websites and consoles to ignore.  When this console serves as
  // your host console, it will never contact consoles matching these
  // address patterns and it will never recommend web pages matching
  // these address patterns.
  ignore: [
    // Off-topic since these are commercial services, not personal websites.
    '.*://medium\\.com/.*',
    '.*://substack\\.com/.*',
    '.*://midnight\\.pub/.*',

    // Does not load within the console due to frame-embedding restrictions.
    '.*://cari\\.institute/.*',
    '.*://everynoise\\.com/.*',
    '.*://clarkesworldmagazine\\.com/.*',
    '.*://qntm\\.org/.*',
    '.*://monoskop\\.org/.*',
    '.*://how\\.complexsystems\\.fail/.*',
    '.*://wdl\\.mcdaniel\\.edu/.*',
  ]
}
