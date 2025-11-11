% تشخیص اینکه عدد کامل هست یا نه(یعنی مجموعه تقسیم علیه هاش بغیر خودش برابر
% خودش هست یا نه)
function y = f(a)
x = [];
for i=1:a-1
    if mod(a,i)==0
        x = [x,i];
    end
end
if(sum(x)==a)
    y = 1;
else
    y = 0;
end