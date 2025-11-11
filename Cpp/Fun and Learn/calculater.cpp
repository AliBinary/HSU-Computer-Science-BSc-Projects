#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

float a, b, ans, nums[100];
int N, did;
string ops, again, pm, yesorno;

const char *msg[40] = {
    "\nHow many numbers do you want to add together? ",
    "\nOk, We want to get the sum of some numbers",
    "\nanswer is : ",
    "\nOk, we want to subtract <a> from <b>",
    "\nEnter a : ",
    "\nEnter b : ",
    "\nEnter n : ",
    "\nHow many numbers do you want to multiply together? ",
    "\nOk, we want to get the multiplication of some numbers",
    "\nOk, we want to divide <a> by <b>",
    "\nOk, we want to raise <a> to the power of <b>",
    "\nOk, we want to get the <nth> root of the number <a>",
    "\nOk, we want to calculate the <n>-factorial",
    "\nThe constant value of <Pi> is : ",
    "\nThe constant value of <e> is : ",
    "\nHow many numbers do you want to calculate the average of? ",
    "\nOk, we want to get the inverse of the number <a>",
    "\nOk, we want to get the complement of number <a>",
    "\nPlease Enter The Input Base: ",
    "\nEnter The Number : ",
    "\nPlease Enter The Output Base: ",
    "\nWhich unit do you want to convert to another? (type <D> or <R>)\n ",
    "\nOK, Enter Degrees : ",
    "\nOK, Enter radians : ",
    "\nOk, we want to get the logarithm of the number <a> to the base of <b>",
    "\nOk, we want to get the natural logarithm of the number <a>",
    "\nOk, we want to calculate the value of the exponential function in <a>",
    "\nOK, we want to get Sin(n)",
    "\nOK, we want to get Cos(n)",
    "\nOK, we want to get Tan(n)",
    "\nOK, we want to get Cot(n)",
    "\nIs the input value in radians or degrees? (type <R> or <D>)\n ",
    "\nOK, we want to get Inverse Sine(n)",
    "\nOK, we want to get Inverse Cos(n)",
    "\nOK, we want to get Inverse Tan(n)",
    "\nOK, we want to get Inverse Cot(n)",
    "\nOK, we want to get Hyperbolic Sine(n)",
    "\nOK, we want to get Hyperbolic Cos(n)",
    "\nOK, we want to get Hyperbolic Tan(n)",
    "\nOK, we want to get Hyperbolic Cot(n)",
};

void cin_valid_float(float &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid number, Try again.>\n";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

void cin_valid_int(int &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid number, Try again.>\n";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

void cin_valid_longint(long int &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid number, Try again.>\n";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

void cin_valid_string(string &pm, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> pm;
        if (!cin)
        {
            cout << "\n<Enter a valid Input, Try again.>\n";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

#define WINDOWS 1
void clrscr()
{
#ifdef WINDOWS
    system("cls");
#endif
#ifdef LINUX
    system("clear");
#endif
}

void intro()
{
    printf("\n\n %-30s <Add>", "Addition");
    printf("\n %-30s <Sub>", "Subtract");
    printf("\n %-30s <Mul>", "Multiplication");
    printf("\n %-30s <Div>", "Division");
    printf("\n %-30s <Pow>", "Power");
    printf("\n %-30s <Root>", "Root");
    printf("\n %-30s <Fac>", "Factorial");
    printf("\n %-30s <Pi>", "show const Pi");
    printf("\n %-30s <e>", "show const e");
    printf("\n %-30s <ave>", "average of numbers");
    printf("\n %-30s <rev>", "reverse a number");
    printf("\n %-30s <com>", "complement a number");
    printf("\n %-30s <base>", "Change the base of a number");
    printf("\n %-30s <con>", "Convert degrees to radians and vice versa");
    printf("\n\t<log>  |  <ln>   |  <Exp>");
    printf("\n <Sin>   |   <Cos>  |  <Tan>   |  <Cot>");
    printf("\nTo use their arc, add 'A' to their first operator (e.g. <ASin>)");
    printf("\n <Sinh>  |  <Cosh>  |  <Tanh>  |  <Coth>\n");
    printf("\n>>Or type \"Q\" to Quite the program<<\n");
}

void get_nums()
{
    string cnt;
    for (int i = 1; i <= N; i++)
    {
        switch (i)
        {
        case 1:
            cnt = "first";
            break;

        case 2:
            cnt = "second";
            break;

        case 3:
            cnt = "third";
            break;

        case 4:
            cnt = "fourth";
            break;

        case 5:
            cnt = "fifth";
            break;

        case 6:
            cnt = "sixth";
            break;

        case 7:
            cnt = "seventh";
            break;

        case 8:
            cnt = "eighth";
            break;

        case 9:
            cnt = "ninth";
            break;

        case 10:
            cnt = "tenth";
            break;

        case 11:
            cnt = "eleventh";
            break;

        case 12:
            cnt = "twelfth";
            break;

        default:
            cnt = to_string(i) + "th";
        }

        cnt = "\nEnter the " + cnt + " number: ";
        cin_valid_float(nums[i - 1], cnt);
    }
}

void add()
{
    cin_valid_int(N, msg[0]);

    cout << msg[1];
    get_nums();
    ans = 0;
    for (int i = 0; i < N; i++)
    {
        ans += nums[i];
    }

    cout << msg[2] << ans;
}

void sub()
{
    cout << msg[3];
    cin_valid_float(a, msg[4]);
    cin_valid_float(b, msg[5]);

    ans = a - b;

    cout << msg[2] << ans;
}

void mul()
{
    cin_valid_int(N, msg[7]);
    cout << msg[8];
    get_nums();
    ans = 1;
    for (int i = 0; i < N; i++)
    {
        ans *= nums[i];
    }

    cout << msg[2] << ans;
}

void div()
{
    cout << msg[9];
    cin_valid_float(a, msg[4]);
    cin_valid_float(b, msg[5]);

    ans = a / b;
    cout << msg[2] << ans;
}

void pow()
{
    cout << msg[10];
    cin_valid_float(a, msg[4]);
    cin_valid_float(b, msg[5]);

    ans = pow(a, b);
    cout << msg[2] << ans;
}

void root()
{
    pm = msg[11];
    while (1)
    {

        cout << pm;
        cin_valid_float(a, msg[4]);

        if (a < 0)
        {
            cout << "\nNegative numbers do not have real roots!";
            pm = "\n   enter a positive number to find nth root : ";
            continue;
        }

        cin_valid_float(b, msg[6]);

        ans = pow(a, 1. / b);
        cout << msg[2] << ans;
        break;
    }
}

void fac()
{
    cout << msg[12];
    cin_valid_float(b, msg[6]);

    while (b < 0)
    {
        cout << "\nn must be greater or equal to 0"
             << "\n Please enter a non-negative number : ";
        cin >> b;
    }

    ans = 1;
    for (int i = 1; i <= b; i++)
    {
        ans *= i;
    }
    cout << msg[2] << ans;
}

void pi()
{
    cout << msg[13] << M_PI << endl;
}

void e()
{
    cout << msg[14] << M_E << endl;
}

void ave()
{
    cin_valid_int(N, msg[15]);
    get_nums();
    float sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum += nums[i];
    }
    ans = sum / N;
    cout << msg[2] << ans;
}

void rev()
{
    cout << msg[16];
    cin_valid_int(N, msg[4]);
    pm = to_string(N);
    cout << msg[2];
    for (int i = pm.length(); i >= 0; i--)
    {
        cout << pm[i];
    }
}

void com()
{
    cout << msg[17];
    cin_valid_float(a, msg[4]);
    ans = 1 / a;
    cout << msg[2] << ans;
}

//----------------------------------------------//
char Mychar(long int num)
{
    char a;
    if (num <= 9 && num >= 0)
        a = num + 48;
    else if (num == 10)
        a = 'A';
    else if (num == 11)
        a = 'B';
    else if (num == 12)
        a = 'C';
    else if (num == 13)
        a = 'D';
    else if (num == 14)
        a = 'E';
    else if (num == 15)
        a = 'F';
    return a;
}
//----------------------------------------------//
long int Myflag(long int mabna, char num[])
{
    long int i = 0, counter = 0;
    long int mynum;
    long int flag = 1;

    for (i = 0; num[i] != '\0'; i++)
    {
        if (num[i] >= 48 && num[i] <= 57)
            mynum = num[i] - 48;
        else if (num[i] == 'A' || num[i] == 'a')
            mynum = 10;
        else if (num[i] == 'B' || num[i] == 'b')
            mynum = 11;
        else if (num[i] == 'C' || num[i] == 'c')
            mynum = 12;
        else if (num[i] == 'D' || num[i] == 'd')
            mynum = 13;
        else if (num[i] == 'E' || num[i] == 'e')
            mynum = 14;
        else if (num[i] == 'F' || num[i] == 'f')
            mynum = 15;
        if (mynum >= mabna)
            flag = 0;
    }
    return flag;
}
//----------------------------------------------//
long int Myten(long int mabna, char num[])
{
    long int i = 0, count = 0, counter = 0;
    long int ten = 0;
    long int mynum;
    for (i = 0; num[i] != '\0'; i++)
        counter++;
    counter--;
    for (i = counter; i >= 0; i--)
    {
        if (num[i] >= 48 && num[i] <= 57)
            mynum = num[i] - 48;
        else if (num[i] == 'A' || num[i] == 'a')
            mynum = 10;
        else if (num[i] == 'B' || num[i] == 'b')
            mynum = 11;
        else if (num[i] == 'C' || num[i] == 'c')
            mynum = 12;
        else if (num[i] == 'D' || num[i] == 'd')
            mynum = 13;
        else if (num[i] == 'E' || num[i] == 'e')
            mynum = 14;
        else if (num[i] == 'F' || num[i] == 'f')
            mynum = 15;
        ten = ten + (mynum * pow(mabna, count));
        count++;
    }
    return ten;
}
//----------------------------------------------//
void base()
{
    clrscr();
    long int mabna1, mabna2, count = 0, ten, i, mod;
    char all[100], num[100];

    cin_valid_longint(mabna1, msg[18]);
    while (mabna1 > 16 || mabna1 < 2)
    {
        cout << "\nBase must be between 2 and 16";
        cin_valid_longint(mabna1, msg[18]);
    }

    cout << msg[19];
    cin >> all;

    while (!Myflag(mabna1, all))
    {
        cout << "\nThe Number Does Not Math With The Input Base"
             << "\n Please Enter another Number : ";
        cin >> all;
    }
    cin_valid_longint(mabna2, msg[20]);

    ten = Myten(mabna1, all);
    mod = ten % mabna2;
    num[0] = Mychar(mod);
    while (ten >= mabna2)
    {
        ten /= mabna2;
        mod = ten % mabna2;
        count++;
        num[count] = Mychar(mod);
    }
    cout << msg[2];
    for (i = count; i >= 0; i--)
    {
        cout << num[i];
    }
}

void rad_or_deg()
{
    pm = "I don't understand which you chose, degrees or radians?\n ";
    while (tolower(yesorno[0]) != 'd' && tolower(yesorno[0]) != 'r')
    {
        cin_valid_string(yesorno, pm);
    }
}

void con()
{
    cin_valid_string(yesorno, msg[21]);
    rad_or_deg();
    if (tolower(yesorno[0]) == 'd')
    {
        cin_valid_float(a, msg[22]);
        ans = a * M_PI / 180;
        cout << "\nRadians result: " << ans;
    }
    else
    {
        cin_valid_float(a, msg[23]);
        ans = a * 180 / M_PI;
        cout << "\nDegrees result: " << ans;
    }
}

void log()
{
    cout << msg[24];
    cin_valid_float(a, msg[4]);
    cin_valid_float(b, msg[5]);
    ans = log(a) / log(b);
    cout << endl
         << msg[2] << ans;
}

void ln()
{
    cout << msg[25];
    cin_valid_float(a, msg[4]);
    ans = log(a);
    cout << endl
         << msg[2] << ans;
}

void exp()
{
    cout << msg[26];
    cin_valid_float(a, msg[4]);
    ans = exp(a);
    cout << endl
         << msg[2] << ans;
}

void sin()
{
    cout << msg[27];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'd')
    {
        ans = sin(a * M_PI / 180);
    }
    else
    {
        ans = sin(a);
    }
    cout << msg[2] << ans;
}

void cos()
{
    cout << msg[28];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'd')
    {
        ans = cos(a * M_PI / 180);
    }
    else
    {
        ans = cos(a);
    }
    cout << msg[2] << ans;
}

void tan()
{
    cout << msg[29];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'd')
    {
        ans = tan(a * M_PI / 180);
    }
    else
    {
        ans = tan(a);
    }
    cout << msg[2] << ans;
}

void cot()
{
    cout << msg[30];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'd')
    {
        ans = 1. / tan(a * M_PI / 180);
    }
    else
    {
        ans = 1. / tan(a);
    }
    cout << msg[2] << ans;
}

void asin()
{
    cout << msg[32];
    cin_valid_float(a, msg[6]);
    ans = asin(a);
    cout << "\nin radians :" << ans;
    ans = ans * 180 / M_PI;
    cout << "\nin degrees :" << ans;
}

void acos()
{
    cout << msg[33];
    cin_valid_float(a, msg[6]);
    ans = acos(a);
    cout << "\nin radians :" << ans;
    ans = ans * 180 / M_PI;
    cout << "\nin degrees :" << ans;
}

void atan()
{
    cout << msg[34];
    cin_valid_float(a, msg[6]);
    ans = atan(a);
    cout << "\nin radians :" << ans;
    ans = ans * 180 / M_PI;
    cout << "\nin degrees :" << ans;
}

void acot()
{
    cout << msg[35];
    cin_valid_float(a, msg[6]);
    ans = atan(1. / a);
    cout << "\nin radians :" << ans;
    ans = ans * 180 / M_PI;
    cout << "\nin degrees :" << ans;
}

void sinh()
{
    cout << msg[36];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'r')
    {
        ans = sinh(a);
    }
    else
    {
        a = a * M_PI / 180;
        ans = sinh(a);
    }
    cout << msg[2] << ans;
}

void cosh()
{
    cout << msg[37];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'r')
    {
        ans = cosh(a);
    }
    else
    {
        a = a * M_PI / 180;
        ans = cosh(a);
    }
    cout << msg[2] << ans;
}

void tanh()
{
    cout << msg[38];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'r')
    {
        ans = tanh(a);
    }
    else
    {
        a = a * M_PI / 180;
        ans = tanh(a);
    }
    cout << msg[2] << ans;
}

void coth()
{
    cout << msg[39];
    cin_valid_string(yesorno, msg[31]);
    rad_or_deg();
    cin_valid_float(a, msg[6]);
    if (tolower(yesorno[0]) == 'r')
    {
        ans = 1. / tanh(a);
    }
    else
    {
        a = a * M_PI / 180;
        ans = 1. / tanh(a);
    }
    cout << msg[2] << ans;
}

int get_ops(string ops)
{
    int len = ops.length();
    for (int i = 0; i < len; i++)
        ops[i] = tolower(ops[i]);

    if (ops == "add")
    {
        clrscr();
        add();
        return 1;
    }
    else if (ops == "sub")
    {
        clrscr();
        sub();
        return 1;
    }
    else if (ops == "mul")
    {
        clrscr();
        mul();
        return 1;
    }
    else if (ops == "div")
    {
        clrscr();
        div();
        return 1;
    }
    else if (ops == "pow")
    {
        clrscr();
        pow();
        return 1;
    }
    else if (ops == "root")
    {
        clrscr();
        root();
        return 1;
    }
    else if (ops == "fac")
    {
        clrscr();
        fac();
        return 1;
    }
    else if (ops == "pi")
    {
        pi();
        return 2;
    }
    else if (ops == "e")
    {
        e();
        return 2;
    }
    else if (ops == "ave")
    {
        clrscr();
        ave();
        return 1;
    }
    else if (ops == "rev")
    {
        clrscr();
        rev();
        return 1;
    }
    else if (ops == "com")
    {
        clrscr();
        com();
        return 1;
    }
    else if (ops == "base")
    {
        clrscr();
        base();
        return 1;
    }
    else if (ops == "con")
    {
        clrscr();
        con();
        return 1;
    }
    else if (ops == "log")
    {
        clrscr();
        log();
        return 1;
    }
    else if (ops == "ln")
    {
        clrscr();
        ln();
        return 1;
    }
    else if (ops == "exp")
    {
        clrscr();
        exp();
        return 1;
    }
    else if (ops == "sin")
    {
        clrscr();
        sin();
        return 1;
    }
    else if (ops == "cos")
    {
        clrscr();
        cos();
        return 1;
    }
    else if (ops == "tan")
    {
        clrscr();
        tan();
        return 1;
    }
    else if (ops == "cot")
    {
        clrscr();
        cot();
        return 1;
    }
    else if (ops == "asin")
    {
        clrscr();
        asin();
        return 1;
    }
    else if (ops == "acos")
    {
        clrscr();
        acos();
        return 1;
    }
    else if (ops == "atan")
    {
        clrscr();
        atan();
        return 1;
    }
    else if (ops == "acot")
    {
        clrscr();
        acot();
        return 1;
    }
    else if (ops == "sinh")
    {
        clrscr();
        sinh();
        return 1;
    }
    else if (ops == "cosh")
    {
        clrscr();
        cosh();
        return 1;
    }
    else if (ops == "tanh")
    {
        clrscr();
        tanh();
        return 1;
    }
    else if (ops == "coth")
    {
        clrscr();
        coth();
        return 1;
    }
    else
    {
        cout << "\noh, unknown comand!\n"
             << " Enter operator again : ";
        return -1;
    }
}

int main()
{
    clrscr();
    cout << "Hello, Welcome to my first 1,000-line program. Yesss, it's a calculator.";
    did = 1;
    while (1)
    {
        if (did != 2)
            intro();
        cout << "\nselect any <operator> to use : ";
        cin >> ops;
        if (ops == "q" || ops == "Q")
            break;

        did = get_ops(ops);

        again = "\nDo you want to use this operator again? (y or n)\n ";
        while (1)
        {
            if (did == 1)
            {
                cin_valid_string(yesorno, again);
                if (tolower(yesorno[0]) == 'y')
                    get_ops(ops);
                else if (tolower(yesorno[0] == 'n'))
                {
                    clrscr();
                    break;
                }
                else
                    again = "\nI do not understand! Use this operator again, type Yes or No : \n ";
            }
            else if (did == 2)
                break;
            else
            {
                cin >> ops;
                did = get_ops(ops);
            }
        }
    }

    clrscr();
    cout << "\nI hope you enjoyed this program <3\n";
    return 0;
}