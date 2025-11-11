class QuestionnaireGroup {
  final int id;
  final String? title;

  QuestionnaireGroup({required this.id, this.title});

  factory QuestionnaireGroup.fromJson(
    Map<String, dynamic> json,
  ) {
    return QuestionnaireGroup(
      id: json['id'],
      title: json['title'],
    );
  }
}
