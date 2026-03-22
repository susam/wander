const wander = { // eslint-disable-line no-unused-vars
  _skipURLCheck: true,
  consoles: ['http://localhost:8000/dev/examples/code-injection-console/mallory/'],
  pages: ['https://example.com/']
}
document.cookie = 'name=alice'
console.log('Alice reads cookie:', document.cookie)
