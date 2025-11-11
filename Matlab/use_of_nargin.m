% طریقه کنترل تعداد ورودی های 
function y = yoyo(a,b,c)
switch nargin
    case 1
        b = 0;c=0;
    case 2
        c = 0;
    otherwise
        a=0;b=0;c=0;
end
y = a+b+c;
return