% calculates factorial x
function y=Fact(x)
s = 1;
for i=1:x
    s = s*i;
end
y = s;
return