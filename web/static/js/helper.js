function GetArabicNumber(number) {
  var charIndex = 0;
  var NumericArabic = "";

  while (charIndex < number.length) {
    switch (number[(charIndex)]) {
      case '.':
        NumericArabic += ".";
        break;

      case '0':
        NumericArabic += "٠";
        break;

      case '1':
        NumericArabic += "١";
        break;

      case '2':
        NumericArabic += "٢";
        break;

      case '3':
        NumericArabic += "٣";
        break;

      case '4':
        NumericArabic += "٤";
        break;

      case '5':
        NumericArabic += "٥";
        break;

      case '6':
        NumericArabic += "٦";
        break;

      case '7':
        NumericArabic += "٧";
        break;

      case '8':
        NumericArabic += "٨";
        break;

      case '9':
        NumericArabic += "٩";
        break;

      default:
        NumericArabic += number[(charIndex)];
        break;
    }
    charIndex++;
  }
  return NumericArabic;
}


function array_divider(count_sublist, data) {
  var result = [];
  var subres = [];

  for (var i=0; i < data.length; i++) {
    subres.push(data[i]);

    if ((i+1)%count_sublist == 0) {
      result.push(subres);
      subres = [];
    }
  }

  if (subres.length > 0) {
    result.push(subres);
  }

  return result;
}