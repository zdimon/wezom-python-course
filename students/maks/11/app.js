var name = 'Dima';
var account = 30;
var bet = 0;

var cards = [
    { url: 'images/6-C.png' },
    { url: 'images/6-D.png' },
    { url: 'images/6-H.png' },
    { url: 'images/6-S.png' },
    { url: 'images/7-C.png' },
    { url: 'images/7-D.png' },
    { url: 'images/7-H.png' },
    { url: 'images/7-S.png' },
    { url: 'images/8-C.png' },
    { url: 'images/8-D.png' },
    { url: 'images/8-H.png' },
    { url: 'images/8-S.png' },
    { url: 'images/9-C.png' },
    { url: 'images/9-D.png' },
    { url: 'images/9-H.png' },
    { url: 'images/9-S.png' },
    { url: 'images/10-C.png' },
    { url: 'images/10-D.png' },
    { url: 'images/10-H.png' },
    { url: 'images/10-S.png' },
    { url: 'images/11-C.png' },
    { url: 'images/11-D.png' },
    { url: 'images/11-H.png' },
    { url: 'images/11-S.png' },



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

// for(var i = 0; i<100; i++) {
//     l(i);
// }

function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

var showCards = function() {

    var div = $('#content');
    var inputbox = $('#count');
    console.log(inputbox.val());
    var header = $('#header').html(inputbox.val());
    div.css('border', '1px solid green');
    // div.hide();
    //console.log(getRandomArbitrary(1,5));

     for(var i = 0; i<inputbox.val(); i++) {
         //l(i);
         div.append(`<img src="${cards[getRandomArbitrary(1,cards.length)].url}" />`);
    }



    // cards.forEach(function(el) {
    //     l(el);
    //     div.append(`<img src="${el.url}" />`);
      
    // });
}

var button = $('#startGame');
button.on('click',showCards);

