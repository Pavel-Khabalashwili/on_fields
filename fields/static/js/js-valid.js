// JUST VALIDATE ---------------------------
// Форма обратной связи
new JustValidate (".js-form-connection", {
    rules:{
  
      name:{
        required: true,
        minLength: 2,
        maxLength: 30,
      },
  
      tel:{
        required: true,
        function: (name, value) => {
          const phone = selector.inputmask.unmaskedvalue();
          console.log(phone);
          return Number(phone) && phone.length ===10;
        },
      },
    },
  
    messages: {
      name: {
        required: 'Поле обязательно к заполнению ',
        minLength:'Необходимо ввести имя целиком',
        maxLength: 'Необходимо ввести только имя',
      },
  
      tel:{
        required: 'Поле обязательно к заполнению ',
        function:'Некорректный ввод',
      },
    },
  
    tooltip: {
      fadeOutTime: 4000,
    },
    colorWrong: 'red',

});