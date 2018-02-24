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
    function countchanger(targetclass, siz) {
      if ($(targetclass).val().length <= siz) {
        $(targetclass).removeClass('overlength');
      } else {
        $(targetclass).addClass('overlength');
      }

    }

    // name
    $('input.textbox.name').on('keypress keyup change paste', function () {
      COUNTER.name.innerHTML = CC.name.value.length;
      countchanger('input.textbox.name', 50);
    });

    // description
    $('input.textbox.description').on('keypress keyup change paste', function () {
        COUNTER.description.innerHTML = CC.description.value.length;
        countchanger('input.textbox.description', 100);
    });

    // location
    $('input.textbox.location').on('keypress keyup change paste', function () {
        COUNTER.location.innerHTML = CC.location.value.length;
        countchanger('input.textbox.location', 200);
    });

  }
}
