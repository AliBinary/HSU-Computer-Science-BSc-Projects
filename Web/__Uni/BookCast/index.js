let MyIndex = 1;
let address = [
    "url('img/book0.jpg')",
    "url('img/book1.jpg')",
    "url('img/book2.jpg')",
    "url('img/book3.jpg')",
    "url('img/book4.jpg')",
    "url('img/book5.jpg')",
    "url('img/book6.jpg')",
    "url('img/book7.jpg')",
    "url('img/book8.jpg')",
    "url('img/book9.jpg')",
    "url('img/book10.jpg')",
    "url('img/book11.jpg')",
    "url('img/book12.jpg')",
    "url('img/book13.jpg')",
    "url('img/book14.jpg')",
    "url('img/book15.jpg')",
];

function next() {
    MyIndex = (MyIndex + 1) % 16;
    show();
    clearTimeout(timer);
    timer = setTimeout(change, 5000);
}
function prev() {
    MyIndex--;
    if (MyIndex < 0) MyIndex = 15;
    show();
    clearTimeout(timer);
    timer = setTimeout(change, 5000);
}

function show() {
    let a1 = MyIndex;
    let a2 = (MyIndex + 1) % 16;
    let a3 = (MyIndex + 2) % 16;
    let a4 = (MyIndex + 3) % 16;
    let a5 = (MyIndex + 4) % 16;
    document.getElementById("s1").style.backgroundImage = address[a1];
    document.getElementById("s2").style.backgroundImage = address[a2];
    document.getElementById("s3").style.backgroundImage = address[a3];
    document.getElementById("s4").style.backgroundImage = address[a4];
    document.getElementById("s5").style.backgroundImage = address[a5];
}
function change() {
    MyIndex = (MyIndex + 1) % 16;
    show();
    timer = setTimeout(change, 3000);
}
change();
function m_over(x) {
    x.style.backgroundColor = "rgba(223,230,233,0.7)";
    document.getElementById("news_text").innerHTML = "تازه های این هفته 😀🚫";
    clearTimeout(timer);
}
function m_out(x) {
    x.style.backgroundColor = "white";
    document.getElementById("news_text").innerHTML = "تازه های این هفته 😍";
    clearTimeout(timer);
    timer = setTimeout(change, 3000);
}

function m_over2(y) {
    y.style.backgroundColor = "rgba(223,230,233,0.7)";
    document.getElementById("off_text").innerHTML =
        "کتاب خوب را خوب بخوانید 😁";
}
function m_out2(y) {
    y.style.backgroundColor = "white";
    document.getElementById("off_text").innerHTML =
        "کتاب هایی که همه باید بخوانند 🤩";
}

function m_over3(z) {
    z.style.backgroundColor = "rgba(223,230,233,0.7)";
    document.getElementById("mood_text").innerHTML =
        "برترین های کنترل استرس، زندگی شاید و... 😌";
    document.getElementById("mood_text").style.paddingRight = "400px";
}
function m_out3(z) {
    z.style.backgroundColor = "white";
    document.getElementById("mood_text").innerHTML = "درمانگر خودتان باشید 🥹";
    document.getElementById("mood_text").style.paddingRight = "500px";
}
// ---------- exit ----------
function exit() {
    if (confirm("میخوای خارج بشی؟ 🤨") == true) {
        window.location.href = "./load_index.html";
    }
}
