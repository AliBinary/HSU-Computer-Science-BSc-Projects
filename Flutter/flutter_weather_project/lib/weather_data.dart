// کلاس مدل داده‌های آب‌وهوا

class WeatherData {
  final String dateTime; // تاریخ و ساعت
  final double temp; // دما
  final String description; // توضیح وضعیت هوا
  final String icon; // آیکون وضعیت هوا
  final int humidity; // رطوبت
  final double windSpeed; // سرعت باد
  final int pressure; // فشار هوا

  WeatherData({
    required this.dateTime,
    required this.temp,
    required this.description,
    required this.icon,
    required this.humidity,
    required this.windSpeed,
    required this.pressure,
  });

  factory WeatherData.fromJson(Map<String, dynamic> json) {
    return WeatherData(
      dateTime: json['dt_txt'],
      temp: json['main']['temp'] - 273.15, // تبدیل دما از کلوین به سلسیوس
      description: json['weather'][0]['description'],
      icon: json['weather'][0]['icon'],
      humidity: json['main']['humidity'],
      windSpeed: (json['wind']['speed'] as num).toDouble(),
      pressure: json['main']['pressure'],
    );
  }
}
