% جمع مقسوم علیه های اول یک عدد داده شده
function y = q(n)
y = [];
b = [];
for i=1:n
    if mod(n,i)==0
        y = [y i];
    end
end
for i=1:numel(y)
    t=0;
    for j=2:y(i)-1
        if mod(y(i),j)==0
            t=t+1;
        end
    end
    if t==0
        b = [b, y(i)];
    end
end
y = sum(b);