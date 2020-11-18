var name = 'Dima';

var cards = [
    { url: 'images/6-C.png' },
    { url: 'images/6-D.png' }
];



var f = function(){
    alert('Hello');
}

var l = function (str) {
    console.log(str);
}

if(name === 'Dima') {
    l('My name is Dima');
} else {

}

for(var i = 0; i<100; i++) {
    l(i);
}


var showCards = function() {

    var div = $('#content');
    div.css('border', '1px solid green');
    // div.hide();


    cards.forEach(function(el) {
        l(el);
        div.append(`<img src="${el.url}" />`);
      
    });
}

var button = $('#startGame');
button.on('click',showCards);

