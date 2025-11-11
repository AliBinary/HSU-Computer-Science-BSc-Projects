let captcha;
function generate() {
    document.getElementById("submit").value = "";
    captcha = document.getElementById("image");
    let uniquechar = "";
    const randomchar =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for (let i = 1; i < 5; i++) {
        uniquechar += randomchar.charAt(Math.random() * randomchar.length);
    }
    captcha.innerHTML = uniquechar;
}

function printmsg() {
    const usr_input = document.getElementById("submit").value;

    if (usr_input == captcha.innerHTML) {
        let s = (document.getElementById("key").innerHTML = "Matched");
        document.getElementById("taeed").disabled = false;
        generate();
    } else {
        let s = (document.getElementById("key").innerHTML = "not Matched");
        generate();
    }
}
function gotourl() {
    window.open("page2.html");
}

function zahra() {
    Swal.fire({
        title: "ثبت نام ",
        text: "میخواهید در سایت ما ثبت نام کنید؟",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "OK",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "",
                text: "به سایت ما خوش امدید",
                icon: "success",
            });
            setTimeout(gotourl, 3000);
        }
    });
}
