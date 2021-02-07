(function(){
  M.AutoInit();

  document.addEventListener('DOMContentLoaded', function() {
    const fixedActionBtn = document.querySelectorAll('.fixed-action-btn');
    const fixedActionBtnInstantces = M.FloatingActionButton.init(fixedActionBtn, {
      direction: 'left',
      hoverEnabled: false
    });

    var slider = document.querySelectorAll('.slider');
    var sliderInstantces = M.Slider.init(slider, {
      interval: 5000
    });

    var chips = document.querySelectorAll('.chips');
    var chipsInstantces = M.Chips.init(chips, {
      placeholder: 'タグ...'
    });

    var datepicker = document.querySelectorAll('.datepicker');
    var datepickerInstances = M.Datepicker.init(datepicker, {
      format: "yyyy-mm-dd",
      defaultDate: new Date(),
      setDefaultDate: true,
      showMonthAfterYear: true,
      i18n:{
        cancel: "キャンセル",
        clear: "クリア",
        done: "完了",
        months: [
          "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"
        ],
        monthsShort: [
          "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"
        ],
        weekdays: [
          "日", "月", "火", "水", "木", "金", "土" 
        ],
        weekdaysShort: [
          "日", "月", "火", "水", "木", "金", "土" 
        ],
        weekdaysAbbrev: [
          "日", "月", "火", "水", "木", "金", "土" 
        ]
      }
    });

    var timepicker = document.querySelectorAll('.timepicker');
    var timepickerInstances = M.Timepicker.init(timepicker, {
      twelveHour: false,
      i18n: {
        cancel: "キャンセル",
        clear: "クリア",
        done: "完了"
      }
    });

  });

})();