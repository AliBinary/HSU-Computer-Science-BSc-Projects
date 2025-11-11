var a, b, op;
function key1() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "1";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "1";
        }
    }
}

function key2() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "2";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "2";
        }
    }
}
function key3() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "3";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "3";
        }
    }
}
function key4() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "4";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "4";
        }
    }
}
function key5() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "5";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "5";
        }
    }
}
function key6() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "6";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "6";
        }
    }
}
function key7() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "7";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "7";
        }
    }
}
function key8() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "8";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "8";
        }
    }
}
function key9() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "9";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "9";
        }
    }
}
function key0() {
    if (document.getElementById("lcd").value.length < 20) {
        if (document.getElementById("lcd").value == "0") {
            document.getElementById("lcd").value = "0";
        } else {
            document.getElementById("lcd").value =
                document.getElementById("lcd").value + "0";
        }
    }
}
function keym() {
    document.getElementById("lcd").value =
        document.getElementById("lcd").value + ".";
    document.getElementById("keymmm").disabled = true;
}
function keyplus() {
    a = document.getElementById("lcd").value;
    op = "+";
    cle();
}
function keyminus() {
    a = document.getElementById("lcd").value;
    op = "-";
    cle();
}
function keymulti() {
    a = document.getElementById("lcd").value;
    op = "*";
    cle();
}
function pow() {
    a = document.getElementById("lcd").value;
    op = "^";
    cle();
}
function keydivid() {
    a = document.getElementById("lcd").value;
    op = "/";
    cle();
}
function fact() {
    a = document.getElementById("lcd").value;
    let x = 1;
    for (let i = 1; i <= a; i++) {
        x = x * i;
    }
    document.getElementById("lcd").value = x;
}

function radi() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.sqrt(parseFloat(a));
}
function SINN() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.sin((a * Math.PI) / 180);
}
function COO() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.cos((a * Math.PI) / 180);
}
function LOOGE() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.log(a);
}
function LOOG() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.log10(a);
}
function TANN() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.tan((a * Math.PI) / 180);
}
function inv() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = 1 / a;
}
function darsad() {
    a = document.getElementById("lcd").value;
    document.getElementById("lcd").value = parseFloat(a) / 100;
}
function del() {
    let x = document.getElementById("lcd").value.length;
    if (x == 1) document.getElementById("lcd").value = "0";
    else
        document.getElementById("lcd").value = document
            .getElementById("lcd")
            .value.slice(0, -1);
}
function keyequal() {
    b = document.getElementById("lcd").value;
    if (op == "+") {
        document.getElementById("lcd").value = parseFloat(a) + parseFloat(b);
    } else if (op == "-") {
        document.getElementById("lcd").value = parseFloat(a) - parseFloat(b);
    } else if (op == "/") {
        document.getElementById("lcd").value = parseFloat(a) / parseFloat(b);
    } else if (op == "*") {
        document.getElementById("lcd").value = parseFloat(a) * parseFloat(b);
    } else if (op == "^") {
        document.getElementById("lcd").value = Math.pow(
            parseFloat(a),
            parseFloat(b)
        );
    }
}

function cle() {
    document.getElementById("lcd").value = "0";
    document.getElementById("keymmm").disabled = false;
}
