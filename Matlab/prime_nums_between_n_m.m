% تمام اعداد اول موجود در بازه ای را برمیگرداند
function y = f(n,m)
y = [];
for i=n:m
    tedad = 0;
    for j=2:i-1
        if mod(i,j)==0
            tedad = tedad + 1;
        end
    end
    if tedad == 0
        y = [y i];
    end
end