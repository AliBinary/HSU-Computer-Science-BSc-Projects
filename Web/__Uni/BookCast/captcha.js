let captcha;
function generate() {
    // Clear old input
    document.getElementById("captcha").value = "";

    // Access the element to store
    // the generated captcha
    captcha = document.getElementById("image");
    let uniquechar = "";

    const randomchar =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Generate captcha for length of
    // 5 with random character
    for (let i = 1; i < 5; i++) {
        uniquechar += randomchar.charAt(Math.random() * randomchar.length);
    }

    // Store generated input
    captcha.innerHTML = uniquechar;
}

function printmsg() {
    const usr_input = document.getElementById("captcha").value;

    // Check whether the input is equal
    // to generated captcha or not
    if (usr_input == captcha.innerHTML) {
        let s = (document.getElementById("submit").innerHTML = "Matched");
        document.getElementById("submit").style.color = "#2ECC71";
        document.getElementById("secure").disabled = false;
        generate();
    } else {
        let s = (document.getElementById("submit").innerHTML = "not Matched");
        document.getElementById("submit").style.color = "#E74C3C";
        document.getElementById("secure").disabled = true;
        generate();
    }
}
