% دوآرایه میگیرد، مرتب میکند، بخش پایین ماتریس اول را به بخش بالای ماتریس
% دوم میچسباند
function y=chasbandan(a,b)
a = sort(a);
b = sort(b);
y = [a(1:length(a)/2) , b((length(b)/2)+1:length(b))];