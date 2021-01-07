import 'package:flutter/material.dart';
import 'constants.dart';

class IconContent extends StatelessWidget {
  final IconData icon;
  final String label;
  final Color iconColour;

  IconContent({this.icon, this.label, this.iconColour});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Icon(
          icon,
          size: 80,
          color: iconColour,
          // color: Color(0XFF8D8E98),
        ),
        SizedBox(height: 15),
        Text(
          label,
          style: klabelTextStyle,
        )
      ],
    );
  }
}
