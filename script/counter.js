if (typeof COUNTER === 'undefined') {
  var COUNTER = {};
  COUNTER.name = 0;
  COUNTER.description = 0;
  COUNTER.location = 0;

  // ToDo:文字数カウント
  function counter(target) {
    var text = document.querySelector('input.textbox.' + target).val();
    return text.length;
  }
}

// イベント追加

// document.onload = function () {
//   ["name", "location", "description"].forEach(function (item) {
//     COUNTER.counter(item);
//   });
// }
