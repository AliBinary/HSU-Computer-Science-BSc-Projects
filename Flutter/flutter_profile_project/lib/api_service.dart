import 'dart:convert';
import 'package:http/http.dart' as http;

/*
{
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
*/

class ApiService {
  static const String baseUrl =
      'https://reqres.in/api'; // برای تست
  static const Map<String, String> defaultHeaders = {
    'Content-Type': 'application/json',
    'x-api-key': 'reqres-free-v1', // کلید API اضافه شده
  };

  static Future<String?> login(
    String email,
    String password,
  ) async {
    final url = Uri.parse('$baseUrl/login');

    try {
      final response = await http.post(
        url,
        headers: defaultHeaders,
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['token'];
      } else {
        // Can you log or manage the error here.
        return null;
      }
    } catch (e) {
      // If you have a network error or anything else, return NULL
      return null;
    }
  }

  // If you have other methods here and be sure to add Defaultheaders header
}
