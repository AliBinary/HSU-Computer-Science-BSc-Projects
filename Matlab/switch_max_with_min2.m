function y=switch_max_with_min2(a)
    Max = a(1,1);
    Min = a(1,1);
    x1 = 1; y1 = 1; x2 = 1; y2 = 1;

    for i=1:size(a,1)
        for j=1:size(a,2)
            if a(i,j) > Max
                Max = a(i,j);
                x1 = i;
                y1 = j;
            elseif a(i,j) < Min
                Min = a(i,j);
                x2 = i;
                y2 = j;
            end
        end
    end
    
    temp = a(x1,y1);
    a(x1,y1) = a(x2,y2);
    a(x2,y2) = temp;
    y = a;