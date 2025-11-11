import 'package:flutter/material.dart';
import 'package:flutter_blogclup/gen/assets.gen.dart';
import 'onboarding.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    Future.delayed(const Duration(seconds: 5)).then((
      value,
    ) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (context) => OnBoardingScreen(),
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
