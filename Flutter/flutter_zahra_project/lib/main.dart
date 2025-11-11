import 'package:flutter/cupertino.dart';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import 'package:flutter_blogclup/article.dart';
import 'package:flutter_blogclup/gen/fonts.gen.dart';
import 'package:flutter_blogclup/home.dart';
import 'package:flutter_blogclup/pexels_api_service.dart';
import 'package:flutter_blogclup/profile.dart';
import 'package:flutter_blogclup/splash.dart';

void main() {
  SystemChrome.setSystemUIOverlayStyle(
    SystemUiOverlayStyle(
      statusBarColor: Colors.white,
      statusBarIconBrightness: Brightness.dark,
      systemNavigationBarColor: Colors.white,
      systemNavigationBarIconBrightness: Brightness.dark,
    ),
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  // static const defaultFontFamily = 'Avenir';
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const primaryTextColor = Color(0xff0D253C);
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
        colorScheme: ColorScheme.light(
          primary: primaryColor,
          onPrimary: Colors.white,
          surface: Colors.white,
          onSurface: primaryTextColor,
          background: Color(0xffFBFCFF),
          onBackground: primaryTextColor,
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.white,
          foregroundColor: primaryTextColor,
          titleSpacing: 32,
        ),
        snackBarTheme: SnackBarThemeData(
          backgroundColor: primaryColor,
        ),
        textTheme: TextTheme(
          titleMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            color: secondaryTextColor,
            fontSize: 18,
            fontWeight: FontWeight.w200,
          ),
          titleLarge: TextStyle(
            fontFamily: FontFamily.avenir,
            fontWeight: FontWeight.bold,
            color: primaryTextColor,
            fontSize: 18,
          ),
          titleSmall: TextStyle(
            fontFamily: FontFamily.avenir,
            fontSize: 14,
            fontWeight: FontWeight.w400,
            color: primaryTextColor,
          ),
          bodyMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            color: secondaryTextColor,
            fontSize: 12,
          ),
          bodyLarge: TextStyle(
            fontFamily: FontFamily.avenir,
            color: primaryTextColor,
            fontSize: 14,
          ),
          bodySmall: TextStyle(
            fontFamily: FontFamily.avenir,
            fontWeight: FontWeight.w700,
            fontSize: 10,
            color: Color(0xff7B8BB2),
          ),
          headlineMedium: TextStyle(
            fontFamily: FontFamily.avenir,
            color: primaryTextColor,
            fontSize: 24,
            fontWeight: FontWeight.w700,
          ),
          headlineSmall: TextStyle(
            fontFamily: FontFamily.avenir,
            fontSize: 20,
            color: primaryTextColor,
            fontWeight: FontWeight.w700,
          ),
        ),
      ),

      home: SplashScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

const int homeIndex = 0;
const int articleIndex = 1;
const int searchIndex = 2;
const int menuIndex = 3;

class _MainScreenState extends State<MainScreen> {
  int selectedScreenIndex = homeIndex;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: _BottomNavigation(
        onTap: (int index) {
          setState(() {
            selectedScreenIndex = index;
          });
        },
        selectedIndex: selectedScreenIndex,
      ),
      body: IndexedStack(
        index: selectedScreenIndex,
        children: [
          HomeScreen(),
          ArticleScreen(),
          SearchScreen(),
          ProfileScreen(),
        ],
      ),
    );
  }
}

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final TextEditingController _controller =
      TextEditingController();
  List<Map<String, String>> _results = [];
  bool _isLoading = false;

  Future<void> _searchImages() async {
    print("Search started for: ${_controller.text}");
    setState(() {
      _isLoading = true;
    });

    try {
      final images = await PexelsApiService.searchImages(
        _controller.text,
      );
      setState(() {
        _results = images;
      });
    } catch (e) {
      // handle error
    } finally {
      setState(() {
        _isLoading = false;
      });
      print("Images: $_results");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            // بخش سرچ
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: _controller,
                      decoration: const InputDecoration(
                        hintText:
                            'Type a place or nature keyword...',
                        border: OutlineInputBorder(),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    onPressed: _searchImages,
                    child: const Text('Search'),
                  ),
                ],
              ),
            ),
            // بخش نتایج یا لودینگ
            Expanded(
              child:
                  _isLoading
                      ? const Center(
                        child: CircularProgressIndicator(),
                      )
                      : ListView.builder(
                        padding: const EdgeInsets.all(16),
                        itemCount: _results.length,
                        itemBuilder: (context, index) {
                          final image = _results[index];
                          return Padding(
                            padding: const EdgeInsets.only(
                              right: 8,
                              left: 8,
                            ),
                            child: Column(
                              crossAxisAlignment:
                                  CrossAxisAlignment.start,
                              children: [
                                ClipRRect(
                                  borderRadius:
                                      BorderRadius.circular(
                                        32,
                                      ),
                                  child: Image.network(
                                    image['url']!,
                                    fit: BoxFit.cover,
                                  ),
                                ),
                                const SizedBox(height: 8),
                                Text(
                                  image['alt'] ??
                                      'No description',
                                  style: Theme.of(context)
                                      .textTheme
                                      .bodyMedium!
                                      .copyWith(
                                        fontWeight:
                                            FontWeight.bold,
                                      ),
                                ),
                                const SizedBox(height: 16),
                              ],
                            ),
                          );
                        },
                      ),
            ),
          ],
        ),
      ),
    );
  }
}

class _BottomNavigation extends StatelessWidget {
  final Function(int index) onTap;
  final int selectedIndex;

  const _BottomNavigation({
    required this.onTap,
    required this.selectedIndex,
  });
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 85,
      child: Stack(
        children: [
          Positioned(
            bottom: 0,
            left: 0,
            right: 0,
            child: Container(
              height: 65,
              decoration: BoxDecoration(
                color: Colors.white,
                boxShadow: [
                  BoxShadow(
                    blurRadius: 20,
                    color: Color(
                      0xff9B8487,
                    ).withOpacity(0.3),
                  ),
                ],
              ),
              child: Row(
                mainAxisAlignment:
                    MainAxisAlignment.spaceEvenly,
                children: [
                  _BottomNavigationItem(
                    iconFileName: 'Home.png',
                    activeIconFileName: 'Home.png',
                    title: 'Home',
                    onTab: () {
                      onTap(homeIndex);
                    },
                    isActive: selectedIndex == homeIndex,
                  ),

                  _BottomNavigationItem(
                    onTab: () {
                      onTap(articleIndex);
                    },
                    isActive: selectedIndex == articleIndex,
                    iconFileName: 'Articles.png',
                    activeIconFileName: 'Articles.png',
                    title: 'Article',
                  ),
                  Expanded(child: Container()),

                  _BottomNavigationItem(
                    onTab: () {
                      onTap(searchIndex);
                    },
                    isActive: selectedIndex == searchIndex,
                    iconFileName: 'Search.png',
                    activeIconFileName: 'Search.png',
                    title: 'Search',
                  ),

                  _BottomNavigationItem(
                    onTab: () {
                      onTap(menuIndex);
                    },
                    isActive: selectedIndex == menuIndex,
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
                  color: Color(0xff376AED),
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

class _BottomNavigationItem extends StatelessWidget {
  final String iconFileName;
  final String activeIconFileName;
  final String title;
  final Function() onTab;
  final bool isActive;

  const _BottomNavigationItem({
    required this.iconFileName,
    required this.activeIconFileName,
    required this.title,
    required this.onTab,
    required this.isActive,
  });
  @override
  Widget build(BuildContext context) {
    final ThemeData themeData = Theme.of(context);
    return Expanded(
      child: InkWell(
        onTap: onTab,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/img/icons/$iconFileName',
              width: 24,
              height: 24,
            ),
            SizedBox(height: 4),
            Text(
              title,
              style: Theme.of(
                context,
              ).textTheme.bodySmall!.apply(
                color:
                    isActive
                        ? themeData.colorScheme.primary
                        : themeData
                            .textTheme
                            .bodySmall!
                            .color,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
