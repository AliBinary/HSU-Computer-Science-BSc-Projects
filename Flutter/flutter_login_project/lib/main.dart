import 'package:flutter/material.dart';
import 'loginpage.dart';

// User Name: 3521314294
// Password: 44444444

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login Demo',
      home: LoginPage(),
      routes: {
        '/loginpage':
            (context) =>
                LoginPage(), // So you can use pushReplacementNamed('/login')
      },
      debugShowCheckedModeBanner: false,
    );
  }
}
