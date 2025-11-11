import 'dart:convert';
import 'package:http/http.dart' as http;

class PexelsApiService {
  static const String _apiKey =
      'VJAsmMuyAuoAPUaNISdTz2QfcA9U6F25PyIFDI3nJrO8B3ZkGSdggTT5';
  static const String _baseUrl =
      'https://api.pexels.com/v1/search';

  static Future<List<Map<String, String>>> searchImages(
    String query,
  ) async {
    final response = await http.get(
      Uri.parse(
        '$_baseUrl?query=$query&per_page=10&page=1',
      ),
      headers: {'Authorization': _apiKey},
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);

      final List photos = data['photos'];
      return photos.map<Map<String, String>>((photo) {
        return {
          'url': photo['src']['medium'],
          'alt': photo['alt'],
        };
      }).toList();
    } else {
      throw Exception('Failed to load images');
    }
  }
}
