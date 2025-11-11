import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_blogclub_project/gen/assets.gen.dart';

class onBoardingScreen extends StatelessWidget {
  const onBoardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final ThemeData themeData = Theme.of(context);
    return Scaffold(
      backgroundColor: themeData.colorScheme.background,
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: Padding(
                padding: const EdgeInsets.only(
                  top: 32,
                  bottom: 8,
                ),
                child:
                    Assets.img.background.onboarding
                        .image(),
              ),
            ),
            Container(
              height: 324,
              decoration: BoxDecoration(
                color: themeData.colorScheme.surface,
                boxShadow: [
                  BoxShadow(
                    blurRadius: 20,
                    color: Colors.black.withOpacity(0.1),
                  ),
                ],
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(32),
                  topRight: Radius.circular(32),
                ),
              ),
              child: Column(
                children: [
                  Container(
                    height: 60,
                    child: Row(
                      children: [
                        ElevatedButton(
                          onPressed: () {},
                          style: ButtonStyle(
                            minimumSize:
                                WidgetStateProperty.all(
                                  Size(84, 60),
                                ),
                            backgroundColor:
                                MaterialStateProperty.all(
                                  Colors.blue,
                                ),
                            iconColor:
                                MaterialStateProperty.all(
                                  Colors.white,
                                ),

                            shape: WidgetStateProperty.all(
                              RoundedRectangleBorder(
                                borderRadius:
                                    BorderRadius.circular(
                                      12,
                                    ),
                              ),
                            ),
                          ),
                          child: const Icon(
                            CupertinoIcons.arrow_right,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
