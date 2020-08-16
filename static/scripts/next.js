
$(document).ready(function() {
    console.log("test");
    $("#postButton").click(function(){
        $.ajax({
			type: "POST",
			url: "/test",
			data: {},
			success: function(result) {
                console.log(result);
                
            },
        });
    });
});