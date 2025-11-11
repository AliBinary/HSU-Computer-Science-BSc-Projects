import 'package:alibinary/api_service.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  ThemeMode _themeMode = ThemeMode.dark;
  bool _heartMode = false;
  Locale _locale = Locale('en');
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      localizationsDelegates: [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: AppLocalizations.supportedLocales,
      locale: _locale,
      theme:
          _themeMode == ThemeMode.dark
              ? MyAppThemeConfig.dark().getTheme(
                _locale.languageCode,
              )
              : MyAppThemeConfig.light().getTheme(
                _locale.languageCode,
              ),
      home: MyHomePage(
        toggleThemeMode: () {
          setState(() {
            _themeMode == ThemeMode.dark
                ? _themeMode = ThemeMode.light
                : _themeMode = ThemeMode.dark;
          });
        },
        toggleHeartMode: () {
          setState(() {
            _heartMode
                ? _heartMode = false
                : _heartMode = true;
          });
        },
        selectedLanguageChanged: (
          _Language newSelecetedLanguageByUser,
        ) {
          setState(() {
            _locale = Locale(
              newSelecetedLanguageByUser.name,
            );
          });
        },
        heartMode: _heartMode,
      ),
    );
  }
}

class MyAppThemeConfig {
  static const String faPrimaryFontFamily = "Vazirmatn";
  final Color primaryColor;
  final Color primaryTextColor;
  final Color secondaryTextColor;
  final Color surfaceColor;
  final Color backgroundColor;
  final Color appBarColor;
  final Brightness brightness;

  MyAppThemeConfig.dark()
    : primaryColor = Colors.white,
      primaryTextColor = Colors.white,
      secondaryTextColor = Colors.white70,
      surfaceColor = Color(0x0dffffff),
      backgroundColor = Color.fromARGB(255, 30, 30, 30),
      appBarColor = Colors.black,
      brightness = Brightness.dark;

  MyAppThemeConfig.light()
    : primaryColor = Colors.grey.shade900,
      primaryTextColor = Colors.grey.shade900,
      secondaryTextColor = Colors.grey.shade900.withOpacity(
        0.8,
      ),
      surfaceColor = Color(0x0d000000),
      backgroundColor = Colors.white,
      appBarColor = Color.fromARGB(255, 235, 235, 235),
      brightness = Brightness.light;

  ThemeData getTheme(String languageCode) {
    return ThemeData(
      // This is the theme of your application.
      //
      // TRY THIS: Try running your application with "flutter run". You'll see
      // the application has a purple toolbar. Then, without quitting the app,
      // try changing the seedColor in the colorScheme below to Colors.green
      // and then invoke "hot reload" (save your changes or press the "hot
      // reload" button in a Flutter-supported IDE, or press "r" if you used
      // the command line to start the app).
      //
      // Notice that the counter didn't reset back to zero; the application
      // state is not lost during the reload. To reset the state, use hot
      // restart instead.
      //
      // This works for code too, not just values: Most code changes can be
      // tested with just a hot reload.
      primarySwatch: Colors.pink,
      primaryColor: primaryColor,
      brightness: brightness,

      dividerColor: surfaceColor,
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ButtonStyle(
          backgroundColor: WidgetStateProperty.all(
            primaryColor,
          ),
          foregroundColor: WidgetStateProperty.all(
            backgroundColor,
          ),
        ),
      ),
      scaffoldBackgroundColor: backgroundColor,
      appBarTheme: AppBarTheme(
        elevation: 0,
        backgroundColor: appBarColor,
        foregroundColor: primaryTextColor,
      ),
      inputDecorationTheme: InputDecorationTheme(
        labelStyle: TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.normal,
        ),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide.none,
        ),
        filled: true,
        fillColor: surfaceColor,
      ),
      textTheme:
          languageCode == 'en'
              ? enPrimaryTextTheme
              : faPrimaryTextTheme,
    );
  }

  TextTheme get enPrimaryTextTheme =>
      GoogleFonts.latoTextTheme(
        TextTheme(
          titleLarge: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            color: primaryColor,
          ),
          titleMedium: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: primaryColor,
          ),
          bodyLarge: TextStyle(
            fontSize: 18,
            color: primaryColor,
          ),
          bodyMedium: TextStyle(
            fontSize: 16,
            height: 1.6,
            color: secondaryTextColor,
          ),
          bodySmall: TextStyle(
            fontSize: 14,
            color: secondaryTextColor,
          ),
          labelLarge: TextStyle(fontSize: 16),
        ),
      );

  TextTheme get faPrimaryTextTheme => TextTheme(
    titleLarge: TextStyle(
      fontSize: 24,
      fontWeight: FontWeight.bold,
      color: primaryColor,
      fontFamily: faPrimaryFontFamily,
    ),
    titleMedium: TextStyle(
      fontSize: 20,
      fontWeight: FontWeight.bold,
      color: primaryColor,
      fontFamily: faPrimaryFontFamily,
    ),
    bodyLarge: TextStyle(
      fontSize: 18,
      color: primaryColor,
      fontFamily: faPrimaryFontFamily,
    ),
    bodyMedium: TextStyle(
      fontSize: 16,
      height: 1.7,
      color: secondaryTextColor,
      fontFamily: faPrimaryFontFamily,
    ),
    bodySmall: TextStyle(
      fontSize: 14,
      color: secondaryTextColor,
      fontFamily: faPrimaryFontFamily,
    ),
    labelLarge: TextStyle(
      fontFamily: faPrimaryFontFamily,
      fontSize: 16,
    ),
  );
}

class MyHomePage extends StatefulWidget {
  final Function() toggleThemeMode;
  final Function() toggleHeartMode;
  final Function(_Language _language)
  selectedLanguageChanged;
  final bool heartMode;

  const MyHomePage({
    super.key,
    required this.toggleThemeMode,
    required this.toggleHeartMode,
    required this.selectedLanguageChanged,
    required this.heartMode,
  });

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  _SkillType _skill = _SkillType.cpp;
  _Language _language = _Language.en;
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  void _updateSelectedSkill(_SkillType skillType) {
    setState(() {
      _skill = skillType;
    });
  }

  void _updateSelectedLanguage(_Language language) {
    widget.selectedLanguageChanged(language);
    setState(() {
      _language = language;
    });
  }

  @override
  Widget build(BuildContext context) {
    final localization = AppLocalizations.of(context)!;
    return Scaffold(
      appBar: AppBar(
        title: Text(localization.profileTitle),
        actions: [
          InkWell(
            onTap: widget.toggleThemeMode,
            child: Padding(
              padding: const EdgeInsets.fromLTRB(
                8,
                0,
                16,
                0,
              ),
              child: Icon(CupertinoIcons.sun_max),
            ),
          ),
        ],
      ),
      body: SingleChildScrollView(
        physics: BouncingScrollPhysics(),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsets.all(32),
              child: Row(
                children: [
                  ClipRRect(
                    borderRadius: BorderRadius.circular(8),
                    child: Image.asset(
                      'assets/images/AliGhanbari.jpg',
                      width: 85,
                      height: 85,
                    ),
                  ),
                  SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      crossAxisAlignment:
                          CrossAxisAlignment.start,
                      children: [
                        Text(
                          localization.name,
                          style:
                              Theme.of(
                                context,
                              ).textTheme.titleMedium,
                        ),
                        SizedBox(height: 2),
                        Text(localization.job),
                        SizedBox(height: 8),
                        Row(
                          children: [
                            Icon(
                              CupertinoIcons.location,
                              size: 14,
                              color:
                                  Theme.of(context)
                                      .textTheme
                                      .bodyMedium!
                                      .color,
                            ),
                            SizedBox(width: 3),
                            Text(
                              localization.location,
                              style:
                                  Theme.of(
                                    context,
                                  ).textTheme.bodySmall,
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),

                  InkWell(
                    onTap: widget.toggleHeartMode,
                    // child: Icon(
                    //   widget.heartMode
                    //       ? CupertinoIcons.heart_fill
                    //       : CupertinoIcons.heart,
                    //   color: Colors.pink,
                    // ),
                    child: AnimatedSwitcher(
                      duration: Duration(milliseconds: 300),
                      transitionBuilder:
                          (child, animation) =>
                              ScaleTransition(
                                scale: animation,
                                child: child,
                              ),
                      child: Icon(
                        widget.heartMode
                            ? CupertinoIcons.heart_fill
                            : CupertinoIcons.heart,
                        key: ValueKey(widget.heartMode),
                        color: Colors.pink,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(
                32,
                0,
                32,
                16,
              ),
              child: Text(
                localization.summary,
                style:
                    Theme.of(context).textTheme.bodyMedium,
              ),
            ),
            Divider(),
            Padding(
              padding: const EdgeInsets.fromLTRB(
                32,
                12,
                32,
                12,
              ),
              child: Row(
                mainAxisAlignment:
                    MainAxisAlignment.spaceBetween,
                children: [
                  Text(localization.selectedLanguage),
                  CupertinoSlidingSegmentedControl<
                    _Language
                  >(
                    groupValue: _language,
                    thumbColor: Colors.pink,
                    children: {
                      _Language.en: Text(
                        localization.enLanguage,
                        style: TextStyle(fontSize: 14),
                      ),
                      _Language.fa: Text(
                        localization.faLanguage,
                        style: TextStyle(fontSize: 14),
                      ),
                    },
                    onValueChanged:
                        (value) =>
                            _updateSelectedLanguage(value!),
                  ),
                ],
              ),
            ),
            Divider(),
            Padding(
              padding: const EdgeInsets.fromLTRB(
                32,
                16,
                32,
                12,
              ),
              child: Row(
                crossAxisAlignment:
                    CrossAxisAlignment.center,
                children: [
                  Text(
                    localization.skills,
                    style: Theme.of(
                      context,
                    ).textTheme.bodyLarge!.copyWith(
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  SizedBox(width: 2),
                  Icon(
                    CupertinoIcons.chevron_down,
                    size: 12,
                  ),
                ],
              ),
            ),
            SizedBox(height: 8),
            Center(
              child: Wrap(
                direction: Axis.horizontal,
                spacing: 4,
                runSpacing: 4,
                children: [
                  Skill(
                    type: _SkillType.git,
                    title: 'Git',
                    imagePath: 'assets/images/Git.png',
                    shadowColor: Colors.red,
                    isActive: _skill == _SkillType.git,
                    onTap: () {
                      _updateSelectedSkill(_SkillType.git);
                    },
                  ),
                  Skill(
                    type: _SkillType.github,
                    title: 'Github',
                    imagePath:
                        'assets/images/Github-Dark.png',
                    shadowColor: Colors.white,
                    isActive: _skill == _SkillType.github,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.github,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.cpp,
                    title: 'Cpp',
                    imagePath: 'assets/images/CPP.png',
                    shadowColor: Colors.blue,
                    isActive: _skill == _SkillType.cpp,
                    onTap: () {
                      _updateSelectedSkill(_SkillType.cpp);
                    },
                  ),
                  Skill(
                    type: _SkillType.python,
                    title: 'Python',
                    imagePath:
                        'assets/images/Python-Dark.png',
                    shadowColor: Colors.yellow,
                    isActive: _skill == _SkillType.python,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.python,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.figma,
                    title: 'Figma',
                    imagePath:
                        'assets/images/Figma-Dark.png',
                    shadowColor: Colors.orange,
                    isActive: _skill == _SkillType.figma,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.figma,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.xd,
                    title: 'Xd',
                    imagePath: 'assets/images/XD.png',
                    shadowColor: Colors.purple,
                    isActive: _skill == _SkillType.xd,
                    onTap: () {
                      _updateSelectedSkill(_SkillType.xd);
                    },
                  ),
                  Skill(
                    type: _SkillType.tailwindCSS,
                    title: 'TailwindCSS',
                    imagePath:
                        'assets/images/TailwindCSS-Dark.png',
                    shadowColor: Colors.blue,
                    isActive:
                        _skill == _SkillType.tailwindCSS,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.tailwindCSS,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.javascript,
                    title: 'JavaScript',
                    imagePath:
                        'assets/images/JavaScript.png',
                    shadowColor: Colors.yellow,
                    isActive:
                        _skill == _SkillType.javascript,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.javascript,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.react,
                    title: 'React',
                    imagePath:
                        'assets/images/React-Dark.png',
                    shadowColor: Colors.lightBlueAccent,
                    isActive: _skill == _SkillType.react,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.react,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.nodejs,
                    title: 'NodeJS',
                    imagePath:
                        'assets/images/NodeJS-Dark.png',
                    shadowColor: Colors.green,
                    isActive: _skill == _SkillType.nodejs,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.nodejs,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.mongodb,
                    title: 'MongoDB',
                    imagePath: 'assets/images/MongoDB.png',
                    shadowColor: Colors.teal,
                    isActive: _skill == _SkillType.mongodb,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.mongodb,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.Postman,
                    title: 'Postman',
                    imagePath: 'assets/images/Postman.png',
                    shadowColor: Colors.deepOrange,
                    isActive: _skill == _SkillType.Postman,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.Postman,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.flutter,
                    title: 'Flutter',
                    imagePath:
                        'assets/images/Flutter-Dark.png',
                    shadowColor: Colors.blueAccent,
                    isActive: _skill == _SkillType.flutter,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.flutter,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.stackoverflow,
                    title: 'StackOverflow',
                    imagePath:
                        'assets/images/StackOverflow-Dark.png',
                    shadowColor: Colors.white,
                    isActive:
                        _skill == _SkillType.stackoverflow,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.stackoverflow,
                      );
                    },
                  ),
                  Skill(
                    type: _SkillType.vscode,
                    title: 'VSCode',
                    imagePath:
                        'assets/images/VSCode-Dark.png',
                    shadowColor: Colors.blue,
                    isActive: _skill == _SkillType.vscode,
                    onTap: () {
                      _updateSelectedSkill(
                        _SkillType.vscode,
                      );
                    },
                  ),
                ],
              ),
            ),
            Divider(),
            Padding(
              padding: const EdgeInsets.fromLTRB(
                32,
                12,
                32,
                12,
              ),
              child: Column(
                crossAxisAlignment:
                    CrossAxisAlignment.start,
                children: [
                  Text(
                    localization.personalInformation,
                    style: Theme.of(
                      context,
                    ).textTheme.bodyLarge!.copyWith(
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  SizedBox(height: 12),
                  TextField(
                    controller: _emailController,
                    decoration: InputDecoration(
                      labelText: localization.email,
                      prefixIcon: Icon(CupertinoIcons.at),
                    ),
                  ),
                  SizedBox(height: 8),
                  TextField(
                    controller: _passwordController,
                    decoration: InputDecoration(
                      labelText: localization.password,
                      prefixIcon: Icon(CupertinoIcons.lock),
                    ),
                  ),
                  SizedBox(height: 12),
                  SizedBox(
                    width: double.infinity,
                    height: 48,
                    child: ElevatedButton(
                      onPressed: () async {
                        ScaffoldMessenger.of(
                          context,
                        ).showSnackBar(
                          SnackBar(
                            content: Text('Connecting...'),
                          ),
                        );
                        final token =
                            await ApiService.login(
                              _emailController.text,
                              _passwordController.text,
                            );

                        if (token != null) {
                          ScaffoldMessenger.of(
                            context,
                          ).showSnackBar(
                            SnackBar(
                              content: Text(
                                // '✅ Success! Token: $token',
                                '✅ Success! Yes you did it 🤩\n\nYou will be redirected to my Github page...',
                              ),
                            ),
                          );

                          // Wait a moment so the user can see the message
                          await Future.delayed(
                            Duration(milliseconds: 5000),
                          );

                          final Uri url = Uri.parse(
                            'https://github.com/AliBinary',
                          );
                          if (!await launchUrl(url)) {
                            throw Exception(
                              'Could not launch $url',
                            );
                          }
                        } else {
                          ScaffoldMessenger.of(
                            context,
                          ).showSnackBar(
                            SnackBar(
                              content: Text(
                                '❌ Login failed!\n\nCan You Find UserName & Password? 🤔\n(reqres.in Fake API)',
                              ),
                            ),
                          );
                        }
                      },

                      child: Text(localization.save),
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

class Skill extends StatelessWidget {
  final _SkillType type;
  final String title;
  final String imagePath;
  final Color shadowColor;
  final bool isActive;
  final Function() onTap;

  const Skill({
    super.key,
    required this.type,
    required this.title,
    required this.imagePath,
    required this.shadowColor,
    required this.isActive,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final BorderRadius defaultBorderRadius =
        BorderRadius.circular(12);

    return InkWell(
      borderRadius: defaultBorderRadius,
      onTap: onTap,
      child: Container(
        width: 90,
        height: 90,
        decoration:
            isActive
                ? BoxDecoration(
                  color: Theme.of(context).dividerColor,
                  borderRadius: defaultBorderRadius,
                )
                : null,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              decoration:
                  isActive
                      ? BoxDecoration(
                        boxShadow: [
                          BoxShadow(
                            color: shadowColor,
                            blurRadius: 25,
                            // spreadRadius: 10,
                          ),
                        ],
                      )
                      : null,
              child: Image.asset(
                imagePath,
                width: 50,
                height: 50,
              ),
            ),
            SizedBox(height: 8),
            Text(
              title,
              style: Theme.of(context).textTheme.labelSmall,
            ),
          ],
        ),
      ),
    );
  }
}

enum _SkillType {
  cpp,
  figma,
  flutter,
  git,
  github,
  javascript,
  mongodb,
  nodejs,
  Postman,
  python,
  react,
  stackoverflow,
  tailwindCSS,
  vscode,
  xd,
}

enum _Language { en, fa }
