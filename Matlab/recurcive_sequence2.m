% دنباله هندسی با جمله اول برابر2 و قدرنسبت 3را بنویسید
function S=recurcive_sequence2(n)
S = 3;
for i=2:n
    S(i) = 2*S(i-1);
end
