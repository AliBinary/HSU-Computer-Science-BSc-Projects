% دنباله بازگشتی زیر را بنویسید
function S=recurcive_sequence(n)
S = [2, 3];
for i=3:n
    S(i) = 2*S(i-1) + 3*S(i-2);
end
