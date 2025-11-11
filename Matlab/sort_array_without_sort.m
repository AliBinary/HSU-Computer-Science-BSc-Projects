% آرایه ای بگیرد و بدون استفاده از تابع آماده سورت آنرا مرتب کنید
function y=f(a)
y = [];
while numel(a) > 0
    [i,id] = max(a);
    y = [y,i];
    a = [a(1:id-1), a(id+1 : numel(a))];
end