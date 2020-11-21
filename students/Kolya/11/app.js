var name = 'Dima';
var balance = 10
var stavka = 1
var cards = [
    {url: 'images/10-C.png'},
	{url: 'images/10-D.png'},
	{url: 'images/10-H.png'},
	{url: 'images/10-S.png'},
	{url: 'images/11-C.png'},
	{url: 'images/11-D.png'},
	{url: 'images/11-H.png'},
	{url: 'images/11-S.png'},
	{url: 'images/6-C.png'},
	{url: 'images/6-D.png'},
	{url: 'images/6-H.png'},
	{url: 'images/6-S.png'},
	{url: 'images/7-C.png'},
	{url: 'images/7-D.png'},
	{url: 'images/7-H.png'},
	{url: 'images/7-S.png'},
	{url: 'images/8-C.png'},
	{url: 'images/8-D.png'},
	{url: 'images/8-H.png'},
	{url: 'images/8-S.png'},
	{url: 'images/9-C.png'},
	{url: 'images/9-D.png'},
	{url: 'images/9-H.png'},
	{url: 'images/9-S.png'}
    
];

var f = function(){
    alert('Hello');
}

var l = function (str) {
    console.log(str);
}
function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}
var showCards = function() {

    var div = $('#content');
    var bal = 0
    //var inputbox = $('#count');
    //console.log(inputbox.val());
    //var header = $('#header').html(inputbox.val());
    //div.css('border', '1px solid green');
    // div.hide();
    //button.remove()
    div.append('<p>')
    var mast = [];
    var max = 0
	for(var i = 0; i < 3; i++) {
		l = cards[getRandomArbitrary(1,cards.length)].url
		if (l[7] < 6){
			bals = l[7]
			bals2 = l[8]
			var mas = l[10]
			//if (mast.includes(mas) === true){
			//	bal = Number(bal) + Number(bals) + Number(bals2)
			//}
			//else{
			//	mast.append(mas);
			//}
			console.log(mas)
			if ((Number(bals) + Number(bals2)) > max){
				var max = Number(bals) + Number(bals2)
			}
			else{
				var max = max
			}
			
		}
		else{
			var mas = l[9]
			console.log(mas)
			//if (mast.includes(mas) === true){
			//	bal = Number(bal) + Number(l[7])
			//}
			//else{
			//	mast.append(mas);
			//}
			
		}
		
		div.append(`<img src="${l}" id = 'first'/>`);
	if (bal === 0){
		bal = max
	}
	}
	bal = Number(bal)
	div.append(`<div id = "text"><h3>Ваш баланс: ${balance}</h3><h3>Количество очков: ${bal}</h3><h3>Ваша ставка: ${stavka}</h3></div>`)
	//div.append(`<a href="#" id="stop" class="knopka">Упасть</a>`);
	//div.append(`<a href="#" id="go" class="knopka">Начать</a>`);
	//div.append(`<a href="#" id="more" class="knopka">Больше</a>`);
    //cards.forEach(function(el) {
    //    l(el);
    //    div.append(`<img src="${el.url}" />`);
    //  
    //});

}
var stop = function() {
	
    var div = $('#content');
    var spisok = ['stop', 'go', 'more']
    for(var i = 0; i < 3; i++) {
    	var image_x = document.getElementById('first');
		image_x.parentNode.removeChild(image_x);
		var image_x = document.getElementById(spisok[i]);
		image_x.parentNode.removeChild(image_x);
    	
    }
    div.append('<h2>Вы скинули</h2>')

}
var more = function() {
    var div = $('#content');
    document.getElementById('text').parentNode.removeChild(document.getElementById('text'));
    if (stavka < 10){
    	stavka = stavka + 1
    	div.append(`<div id = "text"><h3>Ваш баланс: ${balance}</h3><h3>Ваша ставка: ${stavka}</h3></div>`)
    }
	else{
		div.append(`<div id = "text"><h3>Ваш баланс: ${balance}</h3><h3>Ваша ставка: ${stavka}</h3></div>`)
	}
}
var go = function() {
    var div = $('#content');
    
}
var button = $('#button2');
button.on('click',showCards)

var button2 = $('#stop');
button2.on('click',stop)

var button3 = $('#more');
button3.on('click',more)

var button4 = $('#go');
button4.on('click',go)
