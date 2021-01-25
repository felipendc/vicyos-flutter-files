import 'constants.dart';
import 'input_page.dart';

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
