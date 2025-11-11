import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_login_project/auth_service.dart';
import 'package:flutter_login_project/questionnaire_Gruop.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class QuestionnairePage extends StatefulWidget {
  const QuestionnairePage({super.key});

  @override
  State<QuestionnairePage> createState() =>
      _QuestionnairePageState();
}

class _QuestionnairePageState
    extends State<QuestionnairePage> {
  final _storage = const FlutterSecureStorage();
  List<QuestionnaireGroup> _groups = [];
  bool _isLoading = true;
  String? _error;

  @override
  void initState() {
    super.initState();
    fetchQuestionnaires();
  }

  Future<void> fetchQuestionnaires() async {
    try {
      final token = await _storage.read(key: 'accessToken');
      if (token == null) {
        setState(() => _error = "No token found.");
        return;
      }

      final response = await authenticatedGet(
        Uri.parse(
          'https://botoxprolong.ir/api/QustionnaireGroup',
        ),
        extraHeaders: {
          'accept': 'text/plain',
          'userId': '359',
          'lang': '1',
        },
      );

      if (response.statusCode == 200) {
        final json = jsonDecode(response.body);
        if (json['isSuccesed'] == true) {
          final List<dynamic> data = json['data'];
          setState(() {
            _groups =
                data
                    .map(
                      (e) => QuestionnaireGroup.fromJson(e),
                    )
                    .toList();
            _isLoading = false;
          });
        } else {
          setState(
            () => _error = 'Failed to load questionnaires.',
          );
        }
      } else {
        setState(
          () =>
              _error =
                  'Server error: ${response.statusCode}',
        );
      }
    } catch (e) {
      setState(() => _error = 'Error: $e');
      // use logout method
      await logout(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading)
      return const Center(
        child: CircularProgressIndicator(),
      );
    if (_error != null) return Center(child: Text(_error!));

    return ListView.builder(
      itemCount: _groups.length,
      itemBuilder: (context, index) {
        final group = _groups[index];
        return ListTile(
          title: Text(group.title ?? 'Untitled'),
          leading: Icon(Icons.list_alt),
          trailing: Icon(Icons.arrow_forward_ios),
          onTap: () {
            // Handle navigation to questionnaire detail if needed
          },
        );
      },
    );
  }
}
