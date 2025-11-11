import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_blogclup/gen/assets.gen.dart';

class ArticleScreen extends StatelessWidget {
  const ArticleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    return Scaffold(
      floatingActionButton: Container(
        width: 111,
        height: 48,
        decoration: BoxDecoration(
          color: themeData.colorScheme.primary,
          borderRadius: BorderRadius.circular(12),
          boxShadow: [
            BoxShadow(
              blurRadius: 20,
              color: themeData.colorScheme.primary
                  .withOpacity(0.5),
            ),
          ],
        ),
        child: InkWell(
          onTap: () {
            showSnackBar(context, 'Like Button is clicked');
          },
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Assets.img.icons.thumbs.svg(),
              SizedBox(width: 8),
              Text(
                '2.1K',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w400,
                  color: themeData.colorScheme.onPrimary,
                ),
              ),
            ],
          ),
        ),
      ),
      backgroundColor: themeData.colorScheme.surface,

      body: Stack(
        children: [
          CustomScrollView(
            slivers: [
              SliverAppBar(
                // pinned: true,
                // floating: true,
                title: Text('Article'),
                actions: [
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.more_horiz_rounded),
                  ),
                  const SizedBox(width: 16),
                ],
              ),
              SliverList(
                delegate: SliverChildListDelegate.fixed([
                  Padding(
                    padding: const EdgeInsets.fromLTRB(
                      32,
                      16,
                      32,
                      16,
                    ),
                    child: Text(
                      'Four Things Every Womn Needs To Know',
                      style:
                          themeData
                              .textTheme
                              .headlineMedium,
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(
                      32,
                      0,
                      16,
                      32,
                    ),
                    child: Row(
                      children: [
                        ClipRRect(
                          borderRadius:
                              BorderRadius.circular(12),
                          child: Assets.img.stories.story9
                              .image(
                                height: 48,
                                width: 48,
                                fit: BoxFit.cover,
                              ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment:
                                CrossAxisAlignment.start,
                            children: [
                              Text(
                                'maryam momeny',
                                style: themeData
                                    .textTheme
                                    .bodyLarge!
                                    .copyWith(
                                      fontWeight:
                                          FontWeight.w400,
                                    ),
                              ),
                              const SizedBox(height: 4),
                              Text('4m ago'),
                            ],
                          ),
                        ),
                        IconButton(
                          onPressed: () {
                            showSnackBar(
                              context,
                              'Bookmark button is clicked',
                            );
                          },
                          icon: Icon(
                            CupertinoIcons.bookmark,
                            color:
                                themeData
                                    .colorScheme
                                    .primary,
                          ),
                        ),
                        IconButton(
                          onPressed: () {
                            showSnackBar(
                              context,
                              'Share button is clicked',
                            );
                          },
                          icon: Icon(
                            CupertinoIcons.share,
                            color:
                                themeData
                                    .colorScheme
                                    .primary,
                          ),
                        ),
                      ],
                    ),
                  ),
                  ClipRRect(
                    borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(32),
                      topRight: Radius.circular(32),
                    ),

                    child:
                        Assets.img.background.singlePost
                            .image(),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(
                      32,
                      32,
                      32,
                      16,
                    ),
                    child: Text(
                      'The role of scientific articles in technological progress',
                      style:
                          themeData.textTheme.headlineSmall,
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(
                      32,
                      0,
                      32,
                      32,
                    ),
                    child: Text(
                      'In todays world, scientific and specialized articles play a very important role in the development and spread of technology. These articles are the result of research and experience of experts in various fields of technology that help share new knowledge and findings. Through these articles researchers and engineers can become familiar with the latest achievements and take more innovative paths. Also, technological articles are often the basis for producing new products and improving existing tools. One of the important features of this type of article is that it is up-to-date and focused on solving practical problems.',
                      style: themeData.textTheme.bodyMedium,
                    ),
                  ),
                ]),
              ),
            ],
          ),

          Positioned(
            bottom: 0,
            child: Container(
              width: MediaQuery.of(context).size.width,
              height: 116,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.bottomCenter,
                  end: Alignment.topCenter,
                  colors: [
                    themeData.colorScheme.surface,

                    themeData.colorScheme.surface
                        .withOpacity(0),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  void showSnackBar(BuildContext context, String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        behavior: SnackBarBehavior.fixed,
      ),
    );
  }
}
