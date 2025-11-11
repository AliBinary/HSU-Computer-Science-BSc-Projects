function check_validity() {
    // first, check validity of all inputs!
    var input1 = document.getElementById("email");
    if (input1.checkValidity()) {
        confirm_dialog();
    }
}
function confirm_dialog() {
    Swal.fire({
        title: "Reset Password",
        text: "Password recovery email will be sent to your email.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "yes please send!",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Sent!",
                text: "Recovery Email Sent.",
                icon: "success",
            });
            message_with_auto_close_timer();
        }
    });
}
function message_with_auto_close_timer() {
    let timerInterval;
    Swal.fire({
        title: "Auto close alert!",
        html: "I will close in <b></b> milliseconds.",
        timer: 2000,
        timerProgressBar: true,
        didOpen: () => {
            Swal.showLoading();
            const timer = Swal.getPopup().querySelector("b");
            timerInterval = setInterval(() => {
                timer.textContent = `${Swal.getTimerLeft()}`;
            }, 100);
        },
        willClose: () => {
            clearInterval(timerInterval);
        },
    }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log("I was closed by the timer");
            go_to_link();
        }
    });
}

function go_to_link() {
    location.replace("./login.html");
}
