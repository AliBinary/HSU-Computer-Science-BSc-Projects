import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:http/http.dart' as http;

/// Create a shared secure storage instance
const storage = FlutterSecureStorage();

/// Refresh the access token using the stored refresh token
Future<bool> refreshAccessToken() async {
  final refreshToken = await storage.read(
    key: 'refreshToken',
  );

  if (refreshToken == null) return false;

  final response = await http.post(
    Uri.parse(
      'https://botoxprolong.ir/api/Users/RefreshToken',
    ),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'refreshToken': refreshToken}),
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);

    if (data['isSuccesed'] == true &&
        data['data'].isNotEmpty) {
      final newAccessToken = data['data'][0]['accessToken'];
      final newRefreshToken =
          data['data'][0]['refreshToken'];

      await storage.write(
        key: 'accessToken',
        value: newAccessToken,
      );
      await storage.write(
        key: 'refreshToken',
        value: newRefreshToken,
      );

      return true;
    }
  }

  return false;
}

/// Makes an authenticated GET request, with automatic token refresh
Future<http.Response> authenticatedGet(
  Uri url, {
  Map<String, String>? extraHeaders,
}) async {
  String? token = await storage.read(key: 'accessToken');

  final headers = {
    'Authorization': 'Bearer $token',
    ...?extraHeaders,
  };

  var response = await http.get(url, headers: headers);

  if (response.statusCode == 401) {
    // Try refreshing the token
    final refreshed = await refreshAccessToken();
    if (refreshed) {
      token = await storage.read(key: 'accessToken');
      final retryHeaders = {
        'Authorization': 'Bearer $token',
        ...?extraHeaders,
      };
      response = await http.get(url, headers: retryHeaders);
    } else {
      throw Exception(
        'Session expired. Please login again.',
      );
    }
  }

  return response;
}

Future<void> logout(BuildContext context) async {
  await storage.delete(key: 'accessToken');
  await storage.delete(key: 'refreshToken');
  Navigator.of(context).pushReplacementNamed('/login');
}
