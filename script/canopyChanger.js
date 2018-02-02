window.onload = function() {
  if (typeof CanopyChanger === 'undefined') {
    var CanopyChanger = {};
    CanopyChanger.name = document.getElementById('screen');
    CanopyChanger.description = document.getElementById('Card-des');
    CanopyChanger.location = document.getElementById('Card-location');

    var CC = {};
    CC.name = document.querySelector('input.textbox.name');
    CC.description = document.querySelector('input.textbox.description');
    CC.location = document.querySelector('input.textbox.location');

    // 初回
    // CanopyChanger.name.innerHTML = CC.name.value;
    // CanopyChanger.description.innerHTML = CC.description.value;
    // CanopyChanger.location.innerHTML = CC.location.value;

    // event listener
    CC.name.addEventListener('keypress', ()=> {
      setTimeout(() => { CanopyChanger.name.innerHTML = CC.name.value; }, 1);
    });
    CC.name.addEventListener('change', () => {
      setTimeout(() => { CanopyChanger.name.innerHTML = CC.name.value; }, 1);
    });
    CC.name.addEventListener('paste', () => {
      setTimeout(() => {CanopyChanger.name.innerHTML = CC.name.value;}, 1);
    });

    CC.description.addEventListener('keypress', ()=> {
      setTimeout(() => { CanopyChanger.description.innerHTML = CC.description.value; }, 1);
    });
    CC.description.addEventListener('change', () => {
      setTimeout(() => { CanopyChanger.description.innerHTML = CC.description.value; }, 1);
    });
    CC.description.addEventListener('paste', () => {
      setTimeout(() => {CanopyChanger.description.innerHTML = CC.description.value;}, 1);
    });

    CC.location.addEventListener('keypress', ()=> {
      setTimeout(() => { CanopyChanger.location.innerHTML = CC.location.value; }, 1);
    });
    CC.location.addEventListener('change', () => {
      setTimeout(() => { CanopyChanger.location.innerHTML = CC.location.value; }, 1);
    });
    CC.location.addEventListener('paste', () => {
      setTimeout(() => {CanopyChanger.location.innerHTML = CC.location.value;}, 1);
    });
  }
}

// ToDo:文字入力の反映
