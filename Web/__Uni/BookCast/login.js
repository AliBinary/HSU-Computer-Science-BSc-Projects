function check_validity() {
    // first, check validity of all inputs!
    var input1 = document.getElementById("u_n");
    var input2 = document.getElementById("passw");
    if (input1.checkValidity() && input2.checkValidity()) {
        confirm_dialog();
    }
}
function confirm_dialog() {
    Swal.fire({
        title: "Login",
        text: "Do you want to enter the site?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "yes enter!",
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Welcome!",
                text: "You will be redirected to the main page of our site.",
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
        }
        go_to_link();
    });
}

function go_to_link() {
    location.replace("./load_index.html");
}
