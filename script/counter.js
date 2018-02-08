// count input text and show that.

window.onload = function () {
  if (typeof COUNTER === 'undefined') {
    var COUNTER = {};
    COUNTER.name = document.querySelector('div.name.counter');
    COUNTER.description = document.querySelector('div.description.counter');
    COUNTER.location = document.querySelector('div.location.counter');

    var CC = {};
    CC.name = document.querySelector('input.textbox.name');
    CC.description = document.querySelector('input.textbox.description');
    CC.location = document.querySelector('input.textbox.location');

    // event listener
    // name
    CC.name.addEventListener('keypress', function () {
      setTimeout(function () {
        COUNTER.name.innerHTML = CC.name.value.length;
      }, 1);
    });
    CC.name.addEventListener('change', function () {
      setTimeout(function () {
        COUNTER.name.innerHTML = CC.name.value.length;
      }, 1);
    });
    CC.name.addEventListener('paste', function () {
      setTimeout(function () {
        COUNTER.name.innerHTML = CC.name.value.length;
      }, 1);
    });

    // description
    CC.description.addEventListener('keypress', function () {
      setTimeout(function () {
        COUNTER.description.innerHTML = CC.description.value.length;
      }, 1);
    });
    CC.description.addEventListener('change', function () {
      setTimeout(function () {
        COUNTER.description.innerHTML = CC.description.value.length;
      }, 1);
    });
    CC.description.addEventListener('paste', function () {
      setTimeout(function () {
        COUNTER.description.innerHTML = CC.description.value.length;
      }, 1);
    });

    // location
    CC.location.addEventListener('keypress', function () {
      setTimeout(function () {
        COUNTER.location.innerHTML = CC.location.value.length;
      }, 1);
    });
    CC.location.addEventListener('change', function () {
      setTimeout(function () {
        COUNTER.location.innerHTML = CC.location.value.length;
      }, 1);
    });
    CC.location.addEventListener('paste', function () {
      setTimeout(function () {
        COUNTER.location.innerHTML = CC.location.value.length;
      }, 1);
    });

  }
}
