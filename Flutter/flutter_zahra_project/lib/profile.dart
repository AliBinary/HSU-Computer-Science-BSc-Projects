import 'package:flutter/material.dart';
import 'package:flutter_blogclup/data.dart';
import 'package:flutter_blogclup/gen/assets.gen.dart';
import 'package:flutter_blogclup/home.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final ThemeData = Theme.of(context);
    final posts = AppDatabase.posts;

    return Scaffold(
      body: SingleChildScrollView(
        physics: BouncingScrollPhysics(),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            AppBar(
              backgroundColor: ThemeData
                  .colorScheme
                  .background
                  .withOpacity(0),
              title: Text('Profile'),
              actions: [
                IconButton(
                  icon: Icon(Icons.more_horiz_rounded),
                  onPressed: () {},
                ),
                SizedBox(width: 16),
              ],
            ),
            Stack(
              children: [
                Container(
                  margin: EdgeInsets.fromLTRB(
                    32,
                    0,
                    32,
                    64,
                  ),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    color: ThemeData.colorScheme.surface,
                    boxShadow: [
                      BoxShadow(
                        blurRadius: 20,
                        color: ThemeData
                            .colorScheme
                            .onBackground
                            .withOpacity(0.1),
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment:
                        CrossAxisAlignment.start,
                    children: [
                      Padding(
                        padding: const EdgeInsets.fromLTRB(
                          24,
                          24,
                          24,
                          24,
                        ),
                        child: Row(
                          children: [
                            ClipRRect(
                              borderRadius:
                                  BorderRadius.circular(12),
                              child: Assets
                                  .img
                                  .stories
                                  .story10
                                  .image(
                                    height: 84,
                                    width: 84,
                                  ),
                            ),
                            SizedBox(width: 16),
                            Expanded(
                              child: Column(
                                crossAxisAlignment:
                                    CrossAxisAlignment
                                        .start,
                                children: [
                                  Text('@Joviedan'),
                                  SizedBox(height: 4),
                                  Text(
                                    'jove Daniel',
                                    style: ThemeData
                                        .textTheme
                                        .bodyLarge!
                                        .copyWith(
                                          fontWeight:
                                              FontWeight
                                                  .w700,
                                          fontSize: 15,
                                        ),
                                  ),
                                  SizedBox(height: 8),
                                  Text(
                                    'UX Designer',
                                    style: ThemeData
                                        .textTheme
                                        .bodyLarge!
                                        .apply(
                                          color:
                                              ThemeData
                                                  .colorScheme
                                                  .primary,
                                        ),
                                  ),
                                ],
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
                          0,
                        ),
                        child: Text(
                          'About me',
                          style:
                              ThemeData
                                  .textTheme
                                  .titleLarge,
                        ),
                      ),

                      Padding(
                        padding: const EdgeInsets.fromLTRB(
                          32,
                          4,
                          32,
                          32,
                        ),
                        child: Text(
                          'Madison Blackstone is a director of user experience design, with experience managing global teams.',
                          style: ThemeData
                              .textTheme
                              .bodyLarge!
                              .copyWith(
                                fontWeight: FontWeight.w200,
                              ),
                        ),
                      ),
                      SizedBox(height: 24),
                    ],
                  ),
                ),

                Positioned(
                  bottom: 32,
                  right: 96,
                  left: 96,

                  child: Container(
                    height: 32,
                    decoration: BoxDecoration(
                      boxShadow: [
                        BoxShadow(
                          blurRadius: 30,
                          color: ThemeData
                              .colorScheme
                              .onBackground
                              .withOpacity(0.8),
                        ),
                      ],
                    ),
                  ),
                ),

                Positioned(
                  bottom: 32,
                  left: 64,
                  right: 64,
                  child: Container(
                    height: 68,
                    decoration: BoxDecoration(
                      color: ThemeData.colorScheme.primary,
                      borderRadius: BorderRadius.circular(
                        12,
                      ),
                    ),
                    child: Row(
                      children: [
                        Expanded(
                          flex: 1,

                          child: Container(
                            decoration: BoxDecoration(
                              color: Color(0xff2151CD),
                              borderRadius:
                                  BorderRadius.circular(12),
                            ),
                            child: Column(
                              mainAxisAlignment:
                                  MainAxisAlignment.center,
                              children: [
                                Text(
                                  '52',
                                  style: TextStyle(
                                    fontSize: 20,
                                    fontWeight:
                                        FontWeight.bold,
                                    color:
                                        ThemeData
                                            .colorScheme
                                            .onPrimary,
                                  ),
                                ),
                                SizedBox(height: 4),
                                Text(
                                  'Post',
                                  style: ThemeData
                                      .textTheme
                                      .bodyLarge!
                                      .copyWith(
                                        fontWeight:
                                            FontWeight.w200,
                                        color:
                                            ThemeData
                                                .colorScheme
                                                .onPrimary,
                                      ),
                                ),
                              ],
                            ),
                          ),
                        ),

                        Expanded(
                          flex: 1,

                          child: Column(
                            mainAxisAlignment:
                                MainAxisAlignment.center,
                            children: [
                              Text(
                                '250',
                                style: TextStyle(
                                  fontSize: 20,
                                  fontWeight:
                                      FontWeight.bold,
                                  color:
                                      ThemeData
                                          .colorScheme
                                          .onPrimary,
                                ),
                              ),
                              SizedBox(height: 4),
                              Text(
                                'Following',
                                style: ThemeData
                                    .textTheme
                                    .bodyLarge!
                                    .copyWith(
                                      fontWeight:
                                          FontWeight.w200,
                                      color:
                                          ThemeData
                                              .colorScheme
                                              .onPrimary,
                                    ),
                              ),
                            ],
                          ),
                        ),

                        Expanded(
                          flex: 1,

                          child: Column(
                            mainAxisAlignment:
                                MainAxisAlignment.center,
                            children: [
                              Text(
                                '4.5K',
                                style: TextStyle(
                                  fontSize: 20,
                                  fontWeight:
                                      FontWeight.bold,
                                  color:
                                      ThemeData
                                          .colorScheme
                                          .onPrimary,
                                ),
                              ),
                              SizedBox(height: 4),
                              Text(
                                'Followers',
                                style: ThemeData
                                    .textTheme
                                    .bodyLarge!
                                    .copyWith(
                                      fontWeight:
                                          FontWeight.w200,
                                      color:
                                          ThemeData
                                              .colorScheme
                                              .onPrimary,
                                    ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
            Container(
              decoration: BoxDecoration(
                color: ThemeData.colorScheme.surface,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(32),
                  topRight: Radius.circular(32),
                ),
              ),
              child: Column(
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(
                      32,
                      16,
                      32,
                      16,
                    ),
                    child: Row(
                      crossAxisAlignment:
                          CrossAxisAlignment.center,
                      children: [
                        Expanded(
                          child: Text(
                            'My Posts',
                            style:
                                ThemeData
                                    .textTheme
                                    .titleLarge,
                          ),
                        ),
                        IconButton(
                          onPressed: () {},
                          icon: Assets.img.icons.grid.svg(),
                        ),
                        IconButton(
                          onPressed: () {},
                          icon:
                              Assets.img.icons.table.svg(),
                        ),
                      ],
                    ),
                  ),
                  for (var i = 0; i < posts.length; i++)
                    Post(post: posts[i]),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
