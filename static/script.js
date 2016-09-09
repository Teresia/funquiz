$( document ).ready(function() {
    console.log( "readyyyyyy!" );
});

$(".btn-answer").click(function(){
	setTimeout(function(){
			$(".submit-button").trigger("click")
		}, 1100);

	});
