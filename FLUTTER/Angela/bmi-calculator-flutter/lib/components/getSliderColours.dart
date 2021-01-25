import 'package:bmi_calculator/constants.dart';
import 'package:bmi_calculator/screens/input_page.dart';

getTopResultColor(Gender selectedGender) {
  if (selectedGender == null) {
    return kaTopResultTextNullColour;
  } else if (selectedGender == Gender.male) {
    return kbottomContainerMaleColor;
  } else if (selectedGender == Gender.female) {
    return kbottomContainerFemaleColor;
  }
}

getActiveTrackColor(Gender selectedGender) {
  if (selectedGender == Gender.male) {
    return kactiveSliderMaleColour;
  } else if (selectedGender == Gender.female) {
    return kactiveSliderFemaleColour;
  }
}

getThumbColor(Gender selectedGender) {
  if (selectedGender == Gender.male) {
    return ksliderMaleThumbColour;
  } else if (selectedGender == Gender.female) {
    return ksliderFemaleThumbColour;
  }
}

getOverlayColor(Gender selectedGender) {
  if (selectedGender == Gender.male) {
    return ksliderMaleColourForOverLay;
  } else if (selectedGender == Gender.female) {
    return ksliderFemaleOverLayColour;
  }
}

getAppBarColor(Gender selectedGender) {
  if (selectedGender == Gender.male) {
    return ksliderMaleThumbColour;
  } else if (selectedGender == Gender.female) {
    return kAppBarColorChanger;
  }
}

getBottomContainerColor(Gender selectedGender) {
  if (selectedGender == null) {
    return kbottomContainerNullColor;
  } else if (selectedGender == Gender.male) {
    return kbottomContainerMaleColor;
  } else if (selectedGender == Gender.female) {
    return kbottomContainerFemaleColor;
  }
}
