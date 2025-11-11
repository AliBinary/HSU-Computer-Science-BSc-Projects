import 'package:flutter/material.dart';
import 'package:flutter_login_project/questionnaire_page.dart';

class UserPanelPage extends StatefulWidget {
  final String fullName; // e.g., 'mohammad shahrabadi'

  const UserPanelPage({super.key, required this.fullName});

  @override
  State<UserPanelPage> createState() =>
      _UserPanelPageState();
}

class _UserPanelPageState extends State<UserPanelPage> {
  int _selectedIndex = 0;

  // Your content pages
  final List<Widget> _pages = [
    Center(child: Text('Home')),
    const QuestionnairePage(),
    Center(child: Text('Botox GPT (AI)')),
    Center(child: Text('Support')),
    Center(child: Text('Report')),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            const CircleAvatar(
              backgroundImage: AssetImage(
                'assets/avatar.png',
              ), // Put your image in assets folder
              radius: 18,
            ),
            const SizedBox(width: 10),
            Text(widget.fullName),
          ],
        ),
      ),
      body: _pages[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
        selectedItemColor: Colors.blue,
        unselectedItemColor: Colors.grey,
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.assignment),
            label: 'Questionnaire',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.smart_toy),
            label: 'Botox GPT',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.support_agent),
            label: 'Support',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.pie_chart),
            label: 'Report',
          ),
        ],
      ),
    );
  }
}
