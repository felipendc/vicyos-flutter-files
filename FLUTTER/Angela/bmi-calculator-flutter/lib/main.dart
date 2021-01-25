import 'package:flutter/material.dart';
import 'constants.dart';
import 'screens/input_page.dart';

void main() {
  runApp(
    BMICalculator(),
  );
}

class BMICalculator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        // Change The Slider Colours at => Constants.dart
        sliderTheme: SliderTheme.of(context).copyWith(
          activeTrackColor: kactiveSliderBaseColour,
          inactiveTrackColor: kinactiveSliderBaseColour,
          thumbColor: ksliderBaseThumbColour,
          overlayColor: ksliderBaseColourForOverlay,
        ),
        primaryColor: Color(0xFF0A0E21),
        scaffoldBackgroundColor: Color(0xFF0A0E21),
      ),
      home: InputPage(),
    );
  }
}
