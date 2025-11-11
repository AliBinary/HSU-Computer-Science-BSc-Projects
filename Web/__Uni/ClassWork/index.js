$(document).ready(function () {
    window.onload = function () {
        $("#d1").hide(1000);
        $("#d2").hide(1000);
        $("#d3").hide(1000);
        $("#d4").hide(1000);
        $("#d5").hide(1000);
    };

    $("#u1").click(function () {
        $("#d1").toggle(1000);
    });
    $("#u1").hover(function () {
        $("#d1").css("background-color", "blue");
    });
    $("#u2").click(function () {
        $("#d2").toggle(1000);
    });
    $("#u2").hover(function () {
        $("#d1").css("background-color", "red");
    });
    $("#u3").click(function () {
        $("#d3").toggle(1000);
    });
    $("#u4").click(function () {
        $("#d4").toggle(1000);
    });
    $("#u5").click(function () {
        $("#d5").toggle(1000);
    });
});
