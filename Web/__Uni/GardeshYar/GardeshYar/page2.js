var myIndex = 0;
var names = [
    "Petra",
    "Chichen Itza",
    "China Wall",
    "Christ The Redeemer",
    "Kolosseum",
    "Machu Picchu",
    "Taj Mahal",
];
var rang = [
    "rgba(229, 142, 38,1.0)",
    "rgba(178, 190, 195,1.0)",
    "rgba(68, 189, 50,1.0)",
    "rgba(72, 126, 176,1.0)",
    "rgba(225, 95, 65,1.0)",
    "rgba(0, 148, 50,1.0)",
    "rgba(47, 54, 64,0.7)",
];

function next() {
    myIndex++;
    if (myIndex > 6) {
        myIndex = 0;
    }
    show();
}
function prev() {
    myIndex--;
    if (myIndex < 0) {
        myIndex = 6;
    }
    show();
}

function show() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[myIndex].style.display = "block";
    document.getElementById("esm").innerHTML = names[myIndex];
    document.getElementById("esm").style.color = rang[myIndex];
}

function move() {
    myIndex++;
    if (myIndex > 6) {
        myIndex = 0;
    }
    show();
    tf = setTimeout(move, 3000);
}
move();

function stop() {
    clearTimeout(tf);
    document.getElementById("esm").style.color = "black";
}
function run() {
    clearTimeout(tf);
    tf = setTimeout(move, 3000);
    document.getElementById("esm").style.color = rang[myIndex];
}

// از این قسمت برای اسلایدر بعدی است

let x = 0;
let y = [
    "url(./photo/chin.jpg)",
    "url(./photo/41.jpg)",
    "url(./photo/69.jpg)",
    "url(./photo/73.jpg)",
    "url(./photo/61.jpg)",
    "url(./photo/sfahan.jpg)",
    "url(./photo/shiraz.jpg)",
    "url(./photo/kish2.jpg)",
];
let z = [
    "توکیو ، ژاپن",
    "ماسال ، ایران",
    "ونیز ،ایتالیا",
    "پاریس ،فرانسه",
    "جزیره مروارید، قطر",
    "اصفهان ، ایران",
    "شیراز ،ایران",
    "جزیره کیش ،ایران",
];
let d = [
    "شهریور ماه ، تور 10 روزه",
    "خرداد ماه ، تور 3 روزه",
    "مهرماه ، تور 7 روزه",
    "تیرماه ،تور 10",
    "ابان ماه ،تور 5 روزه",
    "مهرماه ،تور 5 روزه اصفهان",
    "مردادماه ،تور 5 روزه",
    "شهریور ماه ،تور 7 روزه ",
];
function neext() {
    x = (x + 1) % 8;
    showw();
    clearTimeout(tz);
    tz = setTimeout(changee, 5000);
}
function preev() {
    x--;
    if (x < 0) x = 7;
    showw();
    clearTimeout(tz);
    tz = setTimeout(changee, 5000);
}
function showw() {
    let c1 = x;
    let c2 = (x + 1) % 8;
    let c3 = (x + 2) % 8;
    let c4 = (x + 3) % 8;
    document.getElementById("f2").style.backgroundImage = y[c1];
    document.getElementById("f3").style.backgroundImage = y[c2];
    document.getElementById("f4").style.backgroundImage = y[c3];
    document.getElementById("f5").style.backgroundImage = y[c4];
    document.getElementById("H1").innerHTML = z[c1];
    document.getElementById("H2").innerHTML = z[c2];
    document.getElementById("H3").innerHTML = z[c3];
    document.getElementById("H4").innerHTML = z[c4];
    document.getElementById("P1").innerHTML = d[c1];
    document.getElementById("P2").innerHTML = d[c2];
    document.getElementById("P3").innerHTML = d[c3];
    document.getElementById("P4").innerHTML = d[c4];
}
function changee() {
    x = (x + 1) % 8;
    showw();
    tz = setTimeout(changee, 3000);
}
changee();
// برای خروج
function showDialog() {
    var result = window.confirm("آیا میخواهید از سایت خارج شوید ؟");

    if (result) {
        window.location.href = "log/login.html";
    } else {
        console.log("User cancelled the action.");
    }
}
//برای اخبار رونده است
let r = 0;
let h = [
    "درهای موزه جواهرات پس از نزدیک به سه سال تعطیلی، دوباره به روی گردشگران باز خواهد شد",
    "دریاچه تار دماوند تا ۱۵ شهریور برای بازدید گردشگران بازگشایی شد",
    "جاده ارتباطی منطقه گردشگری کوه گل بازگشایی شد",
    "بازگشایی ۵۰ درصد مقاصد گردشگری به گزارش سازمان جهانی گردشگری",
    "کشف ۱۷۹ سکه طلایی و مسی در آذربایجان غربی",
];
function matn() {
    r = (r + 1) % 5;
    document.getElementById("tab").innerHTML = h[r];

    setTimeout(matn, 13000);
}
matn();
//برای ماشین حسابه
function cal() {
    if (
        document.getElementById("al2").style.display == "" ||
        document.getElementById("al2").style.display == "none"
    ) {
        document.getElementById("al2").style.display = "block";
    } else {
        document.getElementById("al2").style.display = "none";
    }
}
