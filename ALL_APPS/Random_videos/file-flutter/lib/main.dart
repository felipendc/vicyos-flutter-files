import 'dart:io';
// import 'dart:convert';

void main() {
  String path = "/";
  list(path);
}

void list(String path) {
  try {
    Directory root = Directory(path);
    if (root.existsSync()) {
      for (FileSystemEntity f in root.listSync()) {
        print(f.path);
      }
    }
  } catch (e) {
    print(e.toString());
  }
}
