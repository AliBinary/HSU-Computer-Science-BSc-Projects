import 'package:flutter/material.dart';
import 'package:flutter_login_project/auth_service.dart';
import 'package:flutter_login_project/userpanel.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPage1State();
}

class _LoginPage1State extends State<LoginPage> {
  final TextEditingController _usernameController =
      TextEditingController();
  final TextEditingController _passwordController =
      TextEditingController();

  bool _isLoading = false;
  String? _errorMessage;

  Future<void> login() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    final url = Uri.parse(
      'https://botoxprolong.ir/api/Users/Login',
    );
    final body = {
      "userName": _usernameController.text.trim(),
      "password": _passwordController.text.trim(),
    };

    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'accept': 'text/plain',
        },
        body: jsonEncode(body),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        if (data['isSuccesed'] == true) {
          final accessToken =
              data['data'][0]['accessToken'];
          final refreshToken =
              data['data'][0]['refreshToken'];

          final fullName = data['data'][0]['fullName'];
          await storage.write(
            key: 'accessToken',
            value: accessToken,
          );
          await storage.write(
            key: 'refreshToken',
            value: refreshToken,
          );

          // TODO: Save token securely and navigate to next screen
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(
              builder:
                  (context) =>
                      UserPanelPage(fullName: fullName),
            ),
          );

          print('Login successful. Token: $accessToken');
          print('Full Name: $fullName');
        } else {
          setState(() {
            _errorMessage =
                'Login failed: ${data['message'] ?? ''}';
          });
        }
      } else {
        setState(() {
          _errorMessage =
              'Server error: ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = 'An error occurred: $e';
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _usernameController,
              decoration: const InputDecoration(
                labelText: 'Username',
              ),
            ),
            TextField(
              controller: _passwordController,
              decoration: const InputDecoration(
                labelText: 'Password',
              ),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            _isLoading
                ? const CircularProgressIndicator()
                : ElevatedButton(
                  onPressed: login,
                  child: const Text('Login'),
                ),
            if (_errorMessage != null) ...[
              const SizedBox(height: 10),
              Text(
                _errorMessage!,
                style: const TextStyle(color: Colors.red),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
