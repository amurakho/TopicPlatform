function launch_scrapper(e){
    e.preventDefault()
}

$(document).ready(function (){

    $("#scrapper-launch-form").submit(function (e){

        e.preventDefault();
        var data = $(this).serializeArray();
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: data,
        })
    })
});