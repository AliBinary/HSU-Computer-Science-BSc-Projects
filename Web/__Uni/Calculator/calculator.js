let opr = "0";
let a;
//-------------------------  Digits  -------------------------------
function k0() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "0";
    } else {
        document.getElementById("lcd").value += "0";
        document.getElementById("ce").disabled = false;
    }
}
function k1() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "1";
    } else {
        document.getElementById("lcd").value += "9";
    }
    document.getElementById("ce").disabled = false;
}
function k2() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "2";
    } else {
        document.getElementById("lcd").value += "2";
    }
    document.getElementById("ce").disabled = false;
}
function k3() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "3";
    } else {
        document.getElementById("lcd").value += "3";
    }
    document.getElementById("ce").disabled = false;
}
function k4() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "4";
    } else {
        document.getElementById("lcd").value += "4";
    }
    document.getElementById("ce").disabled = false;
}
function k5() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "5";
    } else {
        document.getElementById("lcd").value += "5";
    }
    document.getElementById("ce").disabled = false;
}
function k6() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "6";
    } else {
        document.getElementById("lcd").value += "6";
    }
    document.getElementById("ce").disabled = false;
}
function k7() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "7";
    } else {
        document.getElementById("lcd").value += "7";
    }
    document.getElementById("ce").disabled = false;
}
function k8() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "8";
    } else {
        document.getElementById("lcd").value += "8";
    }
    document.getElementById("ce").disabled = false;
}
function k9() {
    if (document.getElementById("lcd").value == "0") {
        document.getElementById("lcd").value = "9";
    } else {
        document.getElementById("lcd").value += "9";
    }
    document.getElementById("ce").disabled = false;
}
//-------------------------  Clear  -------------------------------
function CE() {
    document.getElementById("lcd").value = "0";
    document.getElementById("ce").disabled = true;
    document.getElementById("eq").disabled = true;
    opr = "0";
}
//-------------------------  Point  -------------------------------
function POI() {
    document.getElementById("lcd").value += ".";
    document.getElementById("poi").disabled = true;
}
//-------------------------  Binary operators  -------------------------------
function POW() {
    a = document.getElementById("lcd").value;
    a = parseFloat(a);
    opr = "pow";
    document.getElementById("lcd").value = "0";
    document.getElementById("eq").disabled = false;
    document.getElementById("poi").disabled = false;

    document.getElementById("pow").disabled = true;
    document.getElementById("di").disabled = false;
    document.getElementById("mu").disabled = false;
    document.getElementById("mi").disabled = false;
    document.getElementById("pl").disabled = false;
}
function DI() {
    a = document.getElementById("lcd").value;
    a = parseFloat(a);
    opr = "di";
    document.getElementById("lcd").value = "0";
    document.getElementById("eq").disabled = false;
    document.getElementById("poi").disabled = false;

    document.getElementById("pow").disabled = false;
    document.getElementById("di").disabled = true;
    document.getElementById("mu").disabled = false;
    document.getElementById("mi").disabled = false;
    document.getElementById("pl").disabled = false;
}
function MU() {
    a = document.getElementById("lcd").value;
    a = parseFloat(a);
    opr = "mu";
    document.getElementById("lcd").value = "0";
    document.getElementById("eq").disabled = false;
    document.getElementById("poi").disabled = false;

    document.getElementById("pow").disabled = false;
    document.getElementById("di").disabled = false;
    document.getElementById("mu").disabled = true;
    document.getElementById("mi").disabled = false;
    document.getElementById("pl").disabled = false;
}
function MI() {
    a = document.getElementById("lcd").value;
    a = parseFloat(a);
    opr = "mi";
    document.getElementById("lcd").value = "0";
    document.getElementById("eq").disabled = false;
    document.getElementById("poi").disabled = false;

    document.getElementById("pow").disabled = false;
    document.getElementById("di").disabled = false;
    document.getElementById("mu").disabled = false;
    document.getElementById("mi").disabled = true;
    document.getElementById("pl").disabled = false;
}
function PL() {
    a = document.getElementById("lcd").value;
    a = parseFloat(a);
    opr = "pl";
    document.getElementById("lcd").value = "0";
    document.getElementById("eq").disabled = false;
    document.getElementById("poi").disabled = false;

    document.getElementById("pow").disabled = false;
    document.getElementById("di").disabled = false;
    document.getElementById("mu").disabled = false;
    document.getElementById("mi").disabled = false;
    document.getElementById("pl").disabled = true;
}
//-------------------------  One-number operators  -------------------------------
function RA() {
    let x = document.getElementById("lcd").value;
    document.getElementById("lcd").value = Math.sqrt(x);
    document.getElementById("poi").disabled = false;
}
function FA() {
    const x = document.getElementById("lcd").value;
    let y = 1;
    for (let i = x; i >= 2; i--) {
        y *= i;
    }
    document.getElementById("lcd").value = y;
    document.getElementById("poi").disabled = false;
}
//-------------------------  Equal  -------------------------------
function EQ() {
    if (opr == "pow") {
        let b = document.getElementById("lcd").value;
        b = parseFloat(b);
        document.getElementById("lcd").value = Math.pow(a, b);
    } else if (opr == "di") {
        let b = document.getElementById("lcd").value;
        b = parseFloat(b);
        document.getElementById("lcd").value = a / b;
    } else if (opr == "mu") {
        let b = document.getElementById("lcd").value;
        b = parseFloat(b);
        document.getElementById("lcd").value = a * b;
    } else if (opr == "mi") {
        let b = document.getElementById("lcd").value;
        b = parseFloat(b);
        document.getElementById("lcd").value = a - b;
    } else if (opr == "pl") {
        let b = document.getElementById("lcd").value;
        b = parseFloat(b);
        document.getElementById("lcd").value = a + b;
    }

    document.getElementById("poi").disabled = false;
    document.getElementById("eq").disabled = true;

    if (document.getElementById("lcd").value != "0") {
        document.getElementById("ce").disabled = false;
    }

    document.getElementById("pow").disabled = false;
    document.getElementById("di").disabled = false;
    document.getElementById("mu").disabled = false;
    document.getElementById("mi").disabled = false;
    document.getElementById("pl").disabled = false;
}
