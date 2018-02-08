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

    // event listener
    CC.name.addEventListener('keypress', function(){
      setTimeout(function(){ CanopyChanger.name.innerHTML = CC.name.value; }, 1);
    });
    CC.name.addEventListener('change', function(){
      setTimeout(function(){ CanopyChanger.name.innerHTML = CC.name.value; }, 1);
    });
    CC.name.addEventListener('paste', function(){
      setTimeout(function(){CanopyChanger.name.innerHTML = CC.name.value;}, 1);
    });

    CC.description.addEventListener('keypress', function(){
      setTimeout(function(){ CanopyChanger.description.innerHTML = CC.description.value; }, 1);
    });
    CC.description.addEventListener('change', function(){
      setTimeout(function(){ CanopyChanger.description.innerHTML = CC.description.value; }, 1);
    });
    CC.description.addEventListener('paste', function(){
      setTimeout(function(){CanopyChanger.description.innerHTML = CC.description.value;}, 1);
    });

    CC.location.addEventListener('keypress', function(){
      setTimeout(function(){ CanopyChanger.location.innerHTML = CC.location.value; }, 1);
    });
    CC.location.addEventListener('change', function(){
      setTimeout(function(){ CanopyChanger.location.innerHTML = CC.location.value; }, 1);
    });
    CC.location.addEventListener('paste', function(){
      setTimeout(function(){CanopyChanger.location.innerHTML = CC.location.value;}, 1);
    });
  }
}
