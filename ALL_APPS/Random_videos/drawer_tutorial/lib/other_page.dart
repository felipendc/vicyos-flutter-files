import 'package:flutter/material.dart';

class OtherPage extends StatelessWidget {
  final String pageText;
  //
  OtherPage(this.pageText);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text(pageText),
      ),
      body: Center(
        child: Text(pageText),
      ),
    );
  }
}
