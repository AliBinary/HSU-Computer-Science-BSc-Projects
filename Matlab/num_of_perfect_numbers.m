% تعدادو خود اعداد کامل بین بازه ای را چاپ میکند
function num_of_perfect_numbers(n,m)
tedad = 0;
x = [];
for i=n:m
    s=0;
    for j=1:i-1
        if mod(i,j)==0
            s = s+j;
        end
    end
    if s == i
        x = [x, i];
        tedad = tedad + 1;
    end
end
sprintf('number of perfect numbers between %d and %d is %d',n,m,tedad)
disp(x)