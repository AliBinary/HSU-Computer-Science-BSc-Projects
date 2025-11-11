% آرایه ای میگیردو عناصر را دوبه دو جابجا میکند
function y = jabejaee(a)
for i=2:2:numel(a)
    temp = a(i);
    a(i) = a(i-1);
    a(i-1) = temp;
end
y = a;