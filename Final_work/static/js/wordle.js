  n = 0
  $(document).ready(function() {
    
  input()  
function input(){ d ='';
    $("button").click(function() {
        d = d+$(this).data('key');
        
        // $(this).data('state','absent');
        $('#game_field tr').eq(n).children("td").eq(d.length-1).text($(this).data('key'));
        
        $(document).on('keydown',function(e) {  // Клавиша BackSpace
        if(e.which == 8) {                      // Удаляет символы из таблицы и набора d
          $('#game_field tr').eq(n).children("td").eq(d.length-1).text('');

          console.log(d.substring(0,d.length-1))
          console.log(d.slice(0,-1))
          d = d.substring(0,d.length-1)

        }});
        
        console.log(n)
        console.log(d)
        if (d.length > 5) {d.slice(0,5)
          console.log(d.slice(0,5))
        setTimeout(send(), 2000);
        setTimeout(alert('Вы заполнили все буквы'), 5000)
          }
        //console.log(d.length)
      });}

      

      //$(document).on('keydown',function(e) {
      //  if(e.which == 46) {input(); n=0}});

    $(document).on('keydown',function(e) {
    if(e.which == 9) {send()}});

function send(){

      form_data = String(d.slice(0,5)); // Собираем все данные из формы
      console.log(form_data, "Собранное слово для отправки на сервер")
          $.ajax({
              type: "POST", // Метод отправки
              url: "wordle", // Путь до html файла отправителя
              data: {'word':form_data},
              success: function () {  // Код в этом блоке выполняется при успешной отправке сообщения
                console.log(n, "Запрос POST")
                  //alert("Ваше сообщение отправлено!");
              }
          })
          .done(function(data) {
              if (data) {
                // $('#game_field tr').eq(n).children("td").eq(0
                // ).text(data.word.word[0]).addClass(data.color[0]);

                // $('#game_field tr').eq(n).children("td").eq(1
                // ).text(data.word.word[1]).addClass(data.color[1]);

                // $('#game_field tr').eq(n).children("td").eq(2
                // ).text(data.word.word[2]).addClass(data.color[2]);

                // $('#game_field tr').eq(n).children("td").eq(3
                // ).text(data.word.word[3]).addClass(data.color[3]);

                // $('#game_field tr').eq(n).children("td").eq(4
                // ).text(data.word.word[4]).addClass(data.color[4]);



                $('#game_field tr').eq(n).children("td").eq(0
                ).addClass(data.color[0]);

                $('#game_field tr').eq(n).children("td").eq(1
                ).addClass(data.color[1]);

                $('#game_field tr').eq(n).children("td").eq(2
                ).addClass(data.color[2]);

                $('#game_field tr').eq(n).children("td").eq(3
                ).addClass(data.color[3]);

                $('#game_field tr').eq(n).children("td").eq(4
                ).addClass(data.color[4]);
                
                $("button").eq('n').addClass('red');
                $(this).data('state','absent')
               console.log(data.word.word.join(''))
               console.log(form_data.toUpperCase())
                  
                d ='';
                n = n+1
                console.log(n, "Заполнение ")

              if (data.word.word.join('') == form_data.toUpperCase()) {
                    alert("Вы угадали")}

                if (n==6){alert("Игра окончена");} 

              }
              else {alert("Слова в списке нет!")};


              //else if (data.error) {alert("Слова в списке нет!");}

          });
          //if (n==6){alert("Игра окончена");}
          //event.preventDefault();
        //alert('You pressed enter!');
        
        }

});
