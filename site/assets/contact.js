// Contact form helper. The form works without this file; this only makes it nicer.
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var email = form.getAttribute('data-fallback-email');
  var message = form.querySelector('#message');

  // "Ask about this work" links pass ?work=Title
  var work = new URLSearchParams(location.search).get('work');
  if (work && !message.value) message.value = 'Hi Kevin, I have a question about "' + work + '".\n\n';

  function status(text) {
    var p = form.querySelector('.form-status');
    if (!p) { p = document.createElement('p'); p.className = 'form-status'; p.setAttribute('role', 'status'); form.appendChild(p); }
    p.textContent = text;
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var data = new FormData(form);
    if (data.get('_gotcha')) return;

    // Formspree not set up yet: open the visitor's email app instead.
    if (form.action.indexOf('YOUR_FORM_ID') !== -1) {
      location.href = 'mailto:' + email +
        '?subject=' + encodeURIComponent('Message from ' + data.get('name')) +
        '&body=' + encodeURIComponent(data.get('message') + '\n\n' + data.get('name') + '\n' + data.get('email'));
      return;
    }

    status('Sending...');
    fetch(form.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        form.reset();
        status("Thank you! Your message was sent. I'll get back to you shortly.");
      })
      .catch(function () {
        status('Sorry, that did not go through. Please email ' + email + ' instead.');
      });
  });
})();
