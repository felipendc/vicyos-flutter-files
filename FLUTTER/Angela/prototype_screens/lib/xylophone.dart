import 'package:audioplayers/audio_cache.dart';
import 'package:flutter/material.dart';
// import 'screen0.dart';

Expanded buildKey({Color color, int soundNumber}) {
  return Expanded(
    child: FlatButton(
      child: Text(""),
      color: color,
      padding: EdgeInsets.all(0),
      onPressed: () {
        final player = AudioCache();
        player.play('note$soundNumber.wav');
      },
    ),
  );
}

class XylophoneApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          leading: GestureDetector(
              child: Icon(Icons.arrow_back),
              onTap: () {
                Navigator.pop(context);
              }),
          centerTitle: true,
          title: Text("Aplicativo Xylophone"),
        ),
        backgroundColor: Colors.black12,
        body: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              buildKey(color: Colors.red, soundNumber: 1),
              buildKey(color: Colors.orange, soundNumber: 2),
              buildKey(color: Colors.yellow, soundNumber: 3),
              buildKey(color: Colors.green, soundNumber: 4),
              buildKey(color: Colors.cyan, soundNumber: 5),
              buildKey(color: Colors.blue, soundNumber: 6),
              buildKey(color: Colors.purple, soundNumber: 7),
            ],
          ),
        ),
      ),
    );
  }
}
