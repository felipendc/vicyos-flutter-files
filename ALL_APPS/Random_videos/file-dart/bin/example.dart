import 'dart:io';
// import 'dart:convert';

void main() {
  var myFile = File('/home/vicyos/Imagens/file.txt');

  if (myFile.existsSync()) {
    print('The file exists!');

    print(myFile.path);
    myFile.lastAccessed().then((context) => print(context));

    myFile.rename('/home/vicyos/Imagens/file2.txt');
    myFile.writeAsString('This is the best file ever!');
    myFile.readAsString().then((String contents) => print(contents));
    myFile.deleteSync();
    myFile.length().then((len) => print(len));
  } else {
    myFile.createSync();
  }
  myFile.create();
}
