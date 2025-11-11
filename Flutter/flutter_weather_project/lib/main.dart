import 'dart:convert'; // برای تبدیل JSON به Map
import 'package:flutter/material.dart'; // فریم‌ورک رابط کاربری
import 'package:http/http.dart' as http; // برای ارسال درخواست HTTP
import 'weather_data.dart'; // فایل مدل داده

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weather App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const WeatherScreen(),
    );
  }
}

class WeatherScreen extends StatefulWidget {
  const WeatherScreen({super.key});

  @override
  State<WeatherScreen> createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  late Future<List<WeatherData>> weatherData; // لیست پیش‌بینی آب‌وهوا
  final TextEditingController _cityController = TextEditingController();
  String cityName = "Sabzevar"; // نام پیش‌فرض شهر

  @override
  void initState() {
    super.initState();
    weatherData = getWeatherData(cityName); // بارگذاری داده در شروع
  }

  Future<List<WeatherData>> getWeatherData(String city) async {
    final apiKey = '612b909da4f4b2b2d9855d2f3858b563'; // کلید API شما
    final url =
        'http://api.openweathermap.org/data/2.5/forecast?q=$city&appid=$apiKey';

    final response = await http.get(Uri.parse(url));

    if (response.statusCode == 200) {
      final jsonData = json.decode(response.body);
      final List<dynamic> dataList = jsonData['list'];

      // فقط ۸ بازه اول (۲۴ ساعت آینده)
      final List<WeatherData> forecast =
          dataList.take(8).map((item) {
            return WeatherData.fromJson(item);
          }).toList();

      return forecast;
    } else {
      throw Exception('دریافت اطلاعات هواشناسی ناموفق بود');
    }
  }

  void _searchCity() {
    setState(() {
      cityName = _cityController.text;
      weatherData = getWeatherData(cityName); // دریافت داده برای شهر جدید
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Weather App')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _cityController,
              decoration: InputDecoration(
                labelText: 'نام شهر را وارد کنید',
                border: OutlineInputBorder(),
                prefixIcon: const Icon(Icons.search),
              ),
            ),
            const SizedBox(height: 10),
            ElevatedButton(onPressed: _searchCity, child: const Text('جستجو')),
            const SizedBox(height: 20),
            FutureBuilder<List<WeatherData>>(
              future: weatherData,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const Center(child: CircularProgressIndicator());
                } else if (snapshot.hasError) {
                  return Center(child: Text('خطا: ${snapshot.error}'));
                } else if (snapshot.hasData) {
                  final List<WeatherData> dataList = snapshot.data!;
                  return Expanded(
                    child: ListView.builder(
                      itemCount: dataList.length,
                      itemBuilder: (context, index) {
                        final data = dataList[index];
                        return Card(
                          margin: const EdgeInsets.symmetric(vertical: 8),
                          child: ListTile(
                            leading: Image.network(
                              'http://openweathermap.org/img/wn/${data.icon}@2x.png',
                              width: 50,
                              height: 50,
                            ),
                            title: Text(
                              '${data.dateTime}',
                              style: const TextStyle(
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            subtitle: Text(
                              '🌡 دما: ${data.temp.toStringAsFixed(1)}°C\n'
                              '🌥 وضعیت: ${data.description}\n'
                              '💧 رطوبت: ${data.humidity}% | 💨 باد: ${data.windSpeed} m/s\n'
                              '🔽 فشار: ${data.pressure} hPa',
                            ),
                          ),
                        );
                      },
                    ),
                  );
                }
                return const Center(child: Text('اطلاعاتی موجود نیست'));
              },
            ),
          ],
        ),
      ),
    );
  }
}
