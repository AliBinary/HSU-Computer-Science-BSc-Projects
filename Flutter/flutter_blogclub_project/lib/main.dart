import 'package:dotted_border/dotted_border.dart';
import 'package:flutter/material.dart';
import 'package:flutter_blogclub_project/carousel/carousel_slider.dart';
import 'package:flutter_blogclub_project/data.dart';
import 'package:flutter_blogclub_project/gen/assets.gen.dart';
import 'package:flutter_blogclub_project/gen/fonts.gen.dart';
import 'package:flutter_blogclub_project/splash.dart';

void main() {
  // SystemChrome.setSystemUIOverlayStyle(
  //   SystemUiOverlayStyle(
  //     statusBarColor: Colors.white,
  //     statusBarIconBrightness: Brightness.dark,
  //     systemNavigationBarColor: Colors.white,
  //     systemNavigationBarIconBrightness: Brightness.dark,
  //   ),
  // );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    const primaryTextColor = Color(0xff0D253D);
    const secondaryTextColor = Color(0xff2D4379);
    const primaryColor = Color(0xff376AED);
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        textButtonTheme: TextButtonThemeData(
          style: ButtonStyle(
            textStyle: WidgetStateProperty.all(
              const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w400,
                fontFamily: FontFamily.avenir,
              ),
            ),
          ),
        ),
        colorScheme: const ColorScheme.light(
          primary: primaryColor,
          onPrimary: Colors.white,
          surface: Colors.white,
          onSurface: primaryTextColor,
          background: Color(0xffFBFCFF),
          onBackground: primaryTextColor,
        ),
        textTheme: const TextTheme(
          titleLarge: TextStyle(
            fontFamily: FontFamily.avenir,
            fontWeight: FontWeight.bold,
            fontSize: 18,
            color: primaryTextColor,
          ),
          titleMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            color: secondaryTextColor,
            fontWeight: FontWeight.w200,
            fontSize: 14,
          ),
          titleSmall: TextStyle(
            fontFamily: FontFamily.avenir,
            color: primaryTextColor,
            fontWeight: FontWeight.w400,
            fontSize: 14,
          ),
          headlineMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            fontWeight: FontWeight.w700,
            fontSize: 24,
            color: primaryTextColor,
          ),
          headlineSmall: TextStyle(
            fontFamily: FontFamily.avenir,
            fontSize: 20,
            fontWeight: FontWeight.w700,
            color: primaryTextColor,
          ),
          bodyMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            color: secondaryTextColor,
            fontSize: 12,
          ),
          bodySmall: TextStyle(
            fontFamily: FontFamily.avenir,
            fontWeight: FontWeight.w700,
            color: Color(0xff7B8BB2),
            fontSize: 10,
          ),
        ),
      ),
      /*
      home: Stack(
        children: [
          // Positioned.fill(child: const HomeScreen()),
          Positioned(
            top: 0,
            right: 0,
            left: 0,
            bottom: 50,
            child: const HomeScreen(),
          ),
          Positioned(
            bottom: 0,
            right: 0,
            left: 0,
            child: BottomNavigation(),
          ),
        ],
      ),
      */
      home: const splashScreen(),
    );
  }
}

class BottomNavigation extends StatelessWidget {
  const BottomNavigation({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 85,
      child: Stack(
        children: [
          Positioned(
            left: 0,
            right: 0,
            bottom: 0,
            child: Container(
              height: 65,
              decoration: BoxDecoration(
                color: Colors.white,
                boxShadow: [
                  BoxShadow(
                    blurRadius: 20,
                    color: const Color(0xaa9b8487),
                  ),
                ],
              ),
              child: Row(
                mainAxisAlignment:
                    MainAxisAlignment.spaceEvenly,
                children: [
                  BottomNavigationItem(
                    iconFileName: 'Home.png',
                    activeIconFileName: 'Home.png',
                    title: 'Home',
                  ),
                  BottomNavigationItem(
                    iconFileName: 'Articles.png',
                    activeIconFileName: 'Articles.png',
                    title: 'Articles',
                  ),
                  SizedBox(width: 8),
                  BottomNavigationItem(
                    iconFileName: 'Search.png',
                    activeIconFileName: 'Search.png',
                    title: 'Search',
                  ),
                  BottomNavigationItem(
                    iconFileName: 'Menu.png',
                    activeIconFileName: 'Menu.png',
                    title: 'Menu',
                  ),
                ],
              ),
            ),
          ),
          Center(
            child: Container(
              width: 65,
              height: 85,
              alignment: Alignment.topCenter,
              child: Container(
                height: 65,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(32.5),
                  color: const Color(0xff476AED),
                  border: Border.all(
                    color: Colors.white,
                    width: 4,
                  ),
                ),
                child: Image.asset(
                  'assets/img/icons/plus.png',
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class BottomNavigationItem extends StatelessWidget {
  final String iconFileName;
  final String activeIconFileName;
  final String title;

  const BottomNavigationItem({
    super.key,
    required this.iconFileName,
    required this.activeIconFileName,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Image.asset('assets/img/icons/$iconFileName'),
        SizedBox(height: 4),
        Text(
          title,
          style: Theme.of(context).textTheme.bodySmall,
        ),
      ],
    );
  }
}
