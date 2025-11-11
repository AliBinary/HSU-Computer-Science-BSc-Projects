import 'package:flutter/material.dart';
import 'package:flutter_blogclub_project/gen/assets.gen.dart';
import 'package:flutter_blogclub_project/home.dart';
import 'package:flutter_blogclub_project/onboarding.dart';

class splashScreen extends StatefulWidget {
  const splashScreen({super.key});

  @override
  State<splashScreen> createState() => _splashScreenState();
}

class _splashScreenState extends State<splashScreen> {
  @override
  void initState() {
    Future.delayed(const Duration(seconds: 2)).then((
      value,
    ) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (context) => const onBoardingScreen(),
        ),
      );
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Positioned.fill(
            child: Assets.img.background.splash.image(
              fit: BoxFit.cover,
            ),
          ),
          Center(
            child: Assets.img.icons.logo.svg(width: 100),
          ),
        ],
      ),
    );
  }
}
