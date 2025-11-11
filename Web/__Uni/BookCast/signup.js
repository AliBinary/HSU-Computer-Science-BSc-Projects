function check_validity() {
    // first, check validity of all inputs!
    var input1 = document.getElementById("email");
    var input2 = document.getElementById("num");
    var input3 = document.getElementById("u_n");
    var input4 = document.getElementById("passw");
    if (
        input1.checkValidity() &&
        input2.checkValidity() &&
        input3.checkValidity() &&
        input4.checkValidity()
    ) {
        confirm_dialog();
    }
}
function confirm_dialog() {
    Swal.fire({
        title: "Sign Up",
        text: "Your account will be created in a few moments!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, Create it!",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Welcome!",
                text: "Your account has been created.",
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
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log("I was closed by the timer");
        }
        go_to_link();
    });
}

function go_to_link() {
    location.replace("./login.html");
}
