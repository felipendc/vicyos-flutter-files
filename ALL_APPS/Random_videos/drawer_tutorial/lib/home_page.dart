import 'package:flutter/material.dart';
import './other_page.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String mainProfilePicture =
      "user-accounts-picture/user-pics/felipendc-main.jpg";
  String otherProfilePicture =
      "user-accounts-picture/user-pics/felipendc-second.jpg";

  void switchUser() {
    String backupString = mainProfilePicture;

    setState(() {
      mainProfilePicture = otherProfilePicture;
      otherProfilePicture = backupString;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        child: ListView(
          children: [
            UserAccountsDrawerHeader(
              currentAccountPicture: GestureDetector(
                onTap: () {
                  print("This is the first account picture!");
                },
                child: CircleAvatar(
                  backgroundImage: AssetImage(mainProfilePicture),
                ),
              ),
              accountName: Text("Felipe Ndc"),
              accountEmail: Text("felipendc10@gmail.com"),
              margin: EdgeInsets.all(5),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                // color: Colors.redAccent,
                image: DecorationImage(
                  image:
                      AssetImage("user-accounts-picture/bkground/abstract.jpg"),
                  fit: BoxFit.fill,
                ),
              ),
              otherAccountsPictures: [
                GestureDetector(
                  onTap: () {
                    switchUser();
                  },
                  child: CircleAvatar(
                    backgroundImage: AssetImage(otherProfilePicture),
                  ),
                )
              ],
            ),
            ListTile(
              title: Text("First Page"),
              trailing: Icon(Icons.arrow_upward),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).push(
                  MaterialPageRoute(
                      builder: (BuildContext context) =>
                          OtherPage("First Page")),
                );
              },
            ),
            ListTile(
              title: Text("Second Page"),
              trailing: Icon(Icons.arrow_right),
              onTap: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                      builder: (BuildContext context) =>
                          OtherPage("Second Page")),
                );
              },
            ),
            Divider(),
            ListTile(
              title: Text("Close"),
              trailing: Icon(Icons.cancel),
              onTap: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        ),
      ),
      appBar: AppBar(
        centerTitle: true,
        title: Text("My Drawer App"),
        backgroundColor: Colors.redAccent,
      ),
      body: Center(
        child: Text(
          "HomePage",
          style: TextStyle(fontSize: 35),
        ),
      ),
    );
  }
}
