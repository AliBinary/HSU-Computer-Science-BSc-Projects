function y=switch_max_with_min(a)
    [i,id] = max(a,[],"all");
    [i2,id2] = min(a,[],"all");
    temp = a(id);
    a(id) = a(id2);
    a(id2) = temp;
    y = a;