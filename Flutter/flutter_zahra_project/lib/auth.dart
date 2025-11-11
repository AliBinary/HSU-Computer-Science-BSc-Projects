import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_blogclup/gen/assets.gen.dart';
import 'package:flutter_blogclup/main.dart';
import 'package:http/http.dart' as http;

/*
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
*/

class AuthScrren extends StatefulWidget {
  const AuthScrren({super.key});

  @override
  State<AuthScrren> createState() => _AuthScrrenState();
}

class _AuthScrrenState extends State<AuthScrren> {
  static const int loginTab = 0;
  static const int signUpTab = 1;
  int selectedTabIndex = loginTab;
  @override
  Widget build(BuildContext context) {
    final ThemeData themeData = Theme.of(context);

    final tabTextStyle = TextStyle(
      color: themeData.colorScheme.onPrimary,
      fontSize: 18,
      fontWeight: FontWeight.bold,
    );
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.only(
                bottom: 32,
                top: 32,
              ),
              child: Assets.img.icons.logo.svg(width: 120),
            ),

            Expanded(
              child: Container(
                decoration: BoxDecoration(
                  color: themeData.colorScheme.primary,
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(32),
                    topRight: Radius.circular(32),
                  ),
                ),
                child: Column(
                  children: [
                    SizedBox(
                      height: 60,

                      child: Row(
                        mainAxisAlignment:
                            MainAxisAlignment.spaceEvenly,
                        children: [
                          TextButton(
                            onPressed: () {
                              setState(() {
                                selectedTabIndex = loginTab;
                              });
                            },
                            child: Text(
                              'LOGIN',
                              style: tabTextStyle.apply(
                                color:
                                    selectedTabIndex ==
                                            loginTab
                                        ? Colors.white
                                        : Colors.white54,
                              ),
                            ),
                          ),

                          TextButton(
                            onPressed: () {
                              setState(() {
                                selectedTabIndex =
                                    signUpTab;
                              });
                            },
                            child: Text(
                              'SIGN UP',
                              style: tabTextStyle.apply(
                                color:
                                    selectedTabIndex ==
                                            signUpTab
                                        ? Colors.white
                                        : Colors.white54,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      child: Container(
                        decoration: BoxDecoration(
                          color:
                              themeData.colorScheme.surface,
                          borderRadius: BorderRadius.only(
                            topLeft: Radius.circular(32),
                            topRight: Radius.circular(32),
                          ),
                        ),
                        child: SingleChildScrollView(
                          child: Padding(
                            padding:
                                const EdgeInsets.fromLTRB(
                                  32,
                                  48,
                                  32,
                                  32,
                                ),
                            child:
                                selectedTabIndex == loginTab
                                    ? _Login(
                                      themeData: themeData,
                                    )
                                    : _SignUp(
                                      themeData: themeData,
                                    ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _Login extends StatefulWidget {
  const _Login({super.key, required this.themeData});

  final ThemeData themeData;

  @override
  State<_Login> createState() => _LoginState();
}

class _LoginState extends State<_Login> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _isLoading = false;

  Future<void> _login() async {
    setState(() {
      _isLoading = true;
    });

    final response = await http.post(
      Uri.parse('https://reqres.in/api/login'),
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1',
      },
      body: jsonEncode({
        'email': _emailController.text,
        'password': _passwordController.text,
      }),
    );

    setState(() {
      _isLoading = false;
    });

    if (response.statusCode == 200) {
      final token = jsonDecode(response.body)['token'];
      // لاگین موفق، برو به صفحه اصلی
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (context) => MainScreen(),
        ),
      );
    } else {
      // ارور نمایش بده
      showDialog(
        context: context,
        builder:
            (_) => AlertDialog(
              title: Text('Login Failed'),
              content: Text('Invalid email or password'),
              actions: [
                TextButton(
                  onPressed:
                      () => Navigator.of(context).pop(),
                  child: Text('OK'),
                ),
              ],
            ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Welcome back',
          style: widget.themeData.textTheme.headlineMedium,
        ),
        const SizedBox(height: 8),
        Text(
          'Sign in with your account',
          style: widget.themeData.textTheme.titleMedium!
              .apply(fontSizeFactor: 0.8),
        ),
        const SizedBox(height: 16),
        TextField(
          controller: _emailController,
          decoration: InputDecoration(label: Text('Email')),
        ),
        passwordTextField(controller: _passwordController),
        SizedBox(height: 24),

        ElevatedButton(
          onPressed: _isLoading ? null : _login,

          style: ElevatedButton.styleFrom(
            minimumSize: Size(
              MediaQuery.of(context).size.width,
              60,
            ),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
            backgroundColor:
                widget.themeData.colorScheme.primary,
            foregroundColor: Colors.white,
          ),
          child:
              _isLoading
                  ? CircularProgressIndicator(
                    color: Colors.white,
                  )
                  : Text('LOGIN'),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Forgot your password'),
            SizedBox(width: 8),
            TextButton(
              onPressed: () {},
              child: Text('Reset here'),
            ),
          ],
        ),
        SizedBox(height: 16),
        Center(
          child: Text(
            'OR SIGN IN WITH',
            style: TextStyle(letterSpacing: 2),
          ),
        ),
        SizedBox(height: 16),

        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Assets.img.icons.google.image(
              width: 36,
              height: 36,
            ),
            SizedBox(width: 24),
            Assets.img.icons.facebook.image(
              width: 36,
              height: 36,
            ),
            SizedBox(width: 24),
            Assets.img.icons.twitter.image(
              width: 36,
              height: 36,
            ),
          ],
        ),
      ],
    );
  }
}

class _SignUp extends StatelessWidget {
  final _passwordController = TextEditingController();

  final ThemeData themeData;
  _SignUp({super.key, required this.themeData});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Welcome to blog club',
          style: themeData.textTheme.headlineMedium,
        ),
        const SizedBox(height: 8),
        Text(
          'Please enter your information',
          style: themeData.textTheme.titleMedium!.apply(
            fontSizeFactor: 0.8,
          ),
        ),
        const SizedBox(height: 16),
        TextField(
          decoration: InputDecoration(
            label: Text('Fullname'),
          ),
        ),
        TextField(
          decoration: InputDecoration(label: Text('Email')),
        ),
        passwordTextField(controller: _passwordController),

        SizedBox(height: 24),
        ElevatedButton(
          onPressed: () {
            Navigator.of(context).pushReplacement(
              MaterialPageRoute(
                builder: (context) => MainScreen(),
              ),
            );
          },
          style: ButtonStyle(
            minimumSize: MaterialStateProperty.all(
              Size(MediaQuery.of(context).size.width, 60),
            ),
            shape: MaterialStateProperty.all(
              RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
            ),
            backgroundColor: MaterialStateProperty.all(
              themeData.colorScheme.primary,
            ),
            foregroundColor: MaterialStateProperty.all(
              Colors.white,
            ),
          ),

          child: Text('Sign up'),
        ),

        SizedBox(height: 16),
        Center(
          child: Text(
            'OR SIGN UP WITH',
            style: TextStyle(letterSpacing: 2),
          ),
        ),
        SizedBox(height: 16),

        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Assets.img.icons.google.image(
              width: 36,
              height: 36,
            ),
            SizedBox(width: 24),
            Assets.img.icons.facebook.image(
              width: 36,
              height: 36,
            ),
            SizedBox(width: 24),
            Assets.img.icons.twitter.image(
              width: 36,
              height: 36,
            ),
          ],
        ),
      ],
    );
  }
}

class passwordTextField extends StatefulWidget {
  final TextEditingController controller;

  const passwordTextField({
    super.key,
    required this.controller,
  });

  @override
  State<passwordTextField> createState() =>
      _passwordTextFieldState();
}

class _passwordTextFieldState
    extends State<passwordTextField> {
  bool obscureText = true;

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: widget.controller,
      obscureText: obscureText,
      enableSuggestions: false,
      autocorrect: false,
      decoration: InputDecoration(
        label: Text('Password'),
        suffix: InkWell(
          onTap: () {
            setState(() {
              obscureText = !obscureText;
            });
          },
          child: Text(
            obscureText ? 'Show' : 'Hide',
            style: TextStyle(
              fontSize: 14,
              color: Theme.of(context).colorScheme.primary,
            ),
          ),
        ),
      ),
    );
  }
}
