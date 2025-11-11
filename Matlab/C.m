% calculates choose n from m
function y = C(n,m)
if n>= m
    y = Fact(n)/ (Fact(m) * Fact(n-m));
end
return

% calculates factorial x
function y=Fact(x)
s = 1;
for i=1:x
    s = s*i;
end
y = s;
return