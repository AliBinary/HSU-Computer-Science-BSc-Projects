function y = f(a)
s = 0;
for i=1:numel(a)
    if(mod(a(i),2)==0)
        s = s + a(i);
    end
end
y = s;